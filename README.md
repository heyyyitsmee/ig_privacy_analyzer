# Instagram Account Privacy Analyzer

### Purpose : 
This tool was made after years of observing my family and friends use Instagram too comfortably, where often times I felt they were
comprising their privacy without realizing. This tool was made to raise awareness amongst Instagram daily users who may not be
familiar with countless risks that come with using social media, and to educate them on how they can keep their accounts safe.

### Description :

The program for this application has three functions, one of them being the main function. In this function first a pre-trained
machine learning model is loaded into the variable, model. (I trained the machine learning model using pickle module in another file
named train_model.py) Model is loaded into the program using the pickle module (so that it can be deserialzed). This loaded machine
learning model is used later in the program to calculate predicted risk.

Next two lines are just titles on the application. Here you will notice I have used streamlit to make a very simple interactive
web application

After that the section code is written to allow users to assign different levels of importance to different provacy measures via sliders.
The weight selected by the user on the slider is appended to the empty weights list. If no weights are adjusted then the default
weights are used. Weights here actually determine the influence of each question / security measure on the overall privacy score.
I made this feature so that the users can have more autnomy in deciding what privacy measures mean more to them. A personal account may
deem keeping their account private more important than anything else while a business account may want to prioritize reviewing their
followers.

In the next section questions are written and are iterated through to get user response using radio buttons. These responses are
stored numerically in a list.

Next the two lists, weights and responses, are passed as parameters into the calculate_privacy_score() function. In this function
weights are normalized first to ensure that they sum upto 100%. User's privacy score is calculated then accordingly. (By summing up
the product of each response and its corresponding weight) Score is rounded off to 2 decimal places and returned.

Returning to the main function, now the machine learning model is used. First, the user's input is passed into the model as a 2D
Array as input. Returned by the model is the risk prediction which is stored in the variable predicition. After this, based on the user's
response to each question, tips are displayed onto the screen.

Next lines of code are utilized to visualize the overall score breakdown. To show the user how much did each category contribute to the
score. So for each category a weighted privacy score is calculated. Next panda DataFrame is used for visualization. Using matplotlib, a bar
chart is createdto show how much each privacy measure contributes to the privacy score.

Lastly, using fpdf a general report is generated. In the report Privacy score is written, predicted risk level is written and also the tailored
tips. The best part is the report can be saved as pdf on the user's computer. This way the user can save a summary of their result.

### About train_model.py (Training a Machine Learning Model)

The Machine learning model is a very simple one. First, libraries like numpy, pickle and sklearn.tree are imported. Then a small dataset
is defined along with some labels. The core functionality is that a decision tree classifier is trained on the dataset to predict risk levels
based on features. At the end, the trained model is saved.

Overall, in the main code, this model uses binary responses (yes/no) for privacy-related questions

Please note that this ML implementation is not ideal for real world application. A small dataset was used for simplicity's sake.
In the future I many want to expand on this model and make it more ideal for real world application. I specifically designed the dataset
so that it can be scaled. With larger datasets from real user data, the model can become more robust and accurate.

