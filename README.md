# Bank_Loan_Approval_Prediction
Predict a customer is eligible for bank loan or not
Loan Approval Prediction System
Overview
This project is a Flask-based web application that predicts loan approval status using a trained K-Nearest Neighbors (KNN) model. The model uses various customer features to determine if a loan application will be approved or not.

#Features

User Input Form: Users can enter data into a web form to get a prediction on loan approval.
Real-Time Prediction: Uses a trained KNN model to provide predictions based on user input.
Model Training: Includes code to train and evaluate the KNN model using a dataset of bank loan applications.
#Technologies Used
Python: Programming language for backend development.
Flask: Web framework for creating the web application.
Scikit-Learn: For machine learning model and data preprocessing.
Joblib: For model serialization and deserialization.
HTML/CSS/JavaScript: For front-end development.


#Usage
Open the application in your web browser.
Fill out the form with customer information.
Click the "Predict" button to get a loan approval prediction.
Form Fields
Age: Age of the customer (integer).
Income: Annual income in thousands (integer).
Family: Number of family members (integer).
CCAvg: Average monthly spending with the credit card in thousands (float).
Education: Education level (integer: 1 for bachelor's, 2 for master's, 3 for advanced).
Mortgage: Value of home mortgage in thousands (float).
Securities Account: Does the customer have a securities account? (Checkbox: 1 for yes, 0 for no).
CD Account: Does the customer have a CD account? (Checkbox: 1 for yes, 0 for no).
Online: Does the customer use online banking? (Checkbox: 1 for yes, 0 for no).
Credit Card: Does the customer use a credit card issued by the bank? (Checkbox: 1 for yes, 0 for no).


![Home lone](https://github.com/user-attachments/assets/45d7d9af-17b1-483b-852c-095611f3d401)
