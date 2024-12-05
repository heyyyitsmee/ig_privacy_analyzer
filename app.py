import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import numpy as np
import pickle

def calculate_privacy_score(responses, weights):
    normalized_weights = [w/sum(weights)*100 for w in weights]
    score = sum(r * w for r, w in zip(responses, normalized_weights))
    return round(score, 2), normalized_weights

def generate_report(score, tips, prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Instagram Privacy Analyzer Report", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Your Privacy Score: {score}/100", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Predicted Risk Level: {prediction}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Tips for Improving Privacy:\n" + "\n".join(tips))
    return pdf.output(dest="S").encode("latin1")

def main():

    with open("privacy_model.pkl", "rb") as file:
        model = pickle.load(file)

    st.title("Instagram Privacy Analyzer")
    st.write("Evaluate your Instagram privacy and get tailored recommendations.")

    st.write("### Customize Weights for Each Privacy Measure")
    categories = ["Private Account", "Two-Factor Authentication", "Tagged Posts", "Review Followers", "Sensitive Info Sharing"]
    weights = []
    default_weights = [30, 25, 20, 15, 10]

    for i, category in enumerate(categories):
        weight = st.slider(f"Weight for {category}", min_value=0, max_value=50, value=default_weights[i], key=f"weight_{i}")
        weights.append(weight)

    # Questions
    st.write("### Privacy Questions")
    questions = [
        "Is your account set to private?",
        "Do you use two-factor authentication?",
        "Are tagged posts set to 'manual approval'?",
        "Do you regularly review your followers?",
        "Do you avoid sharing sensitive information?"
    ]
    responses = []

    for i, question in enumerate(questions):
        response = st.radio(question, ("Yes", "No"), key=f"response_{i}")
        responses.append(1 if response == "Yes" else 0)

    # Calculating Privacy Score
    score, normalized_weights= calculate_privacy_score(responses, weights)
    st.subheader(f"Your Privacy Score: {score}/100")

    prediction = model.predict([responses])[0]
    st.subheader(f"Predcited Risk Level: {prediction}")

    # Tips
    tips = []
    if responses[0] == 0:
        tips.append("Set your account to private to protect your posts. This limits access to only approved followers.")
    if responses[1] == 0:
        tips.append("Enable two-factor authentication to add an extra layer of security. Go to 'Settings' > 'Security' > 'Two-Factor Authentication' and follow the steps.")
    if responses[2] == 0:
        tips.append("Set tagged posts to 'manual approval' to avoid unwanted exposure to ensure only the tagged posts you approve of appear on your profile. Navigate to 'Settings' > 'Privacy' > 'Tags' and enable manual approval.")
    if responses[3] == 0:
        tips.append("Review your followers regularly and remove suspicious accounts. This helps keep your account secure from potential stalkers or hackers.")
    if responses[4] == 0:
        tips.append("Avoid sharing personal or sensitive information in posts, such as your address or phone number, to reduce risks of identity theft or harassment.")

    st.write("## Tips")
    for tip in tips:
        st.write(f"- {tip}")

    # Visualization
    st.write("### Privacy Score Breakdown")
    breakdown = [responses[i] * weights[i] for i in range(len(questions))]
    df = pd.DataFrame({"Category": categories, "Score": breakdown})

    fig, ax = plt.subplots()
    ax.bar(df["Category"], df["Score"], color="teal")
    ax.set_ylabel("Score")
    ax.tick_params(axis='x', labelsize=6)
    ax.set_title("Privacy Score Breakdown")
    st.pyplot(fig)

    # Downloadable Report
    st.write("### Download Your Privacy Report")
    if st.button("Generate Report"):
        pdf_content = generate_report(score, tips, prediction)
        st.download_button(
            label="Download Report as PDF",
            data=pdf_content,
            file_name="privacy_report.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
