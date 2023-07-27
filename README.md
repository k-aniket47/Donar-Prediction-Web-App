# Donar-Prediction-Web-App

Donar Prediction Using Income Level is a web application built with Streamlit that predicts the likelihood of finding a donor based on their income level. 
The application utilizes an XGBoost model trained on a dataset of income data to make predictions.

## How to Use
When you access the web application, you will see a sidebar with two options: "Home" and "About."

Select "Home" to go to the prediction page.

On the prediction page, you need to provide the following information to predict the income level:

* Age: Slide the age bar to select your age.
* Workclass: Select your workclass from the dropdown list.
* Education Level: Select your highest education level from the dropdown list.
* Education Number: Slide the education number bar to indicate your level of education.
* Marital Status: Select your marital status from the dropdown list.
* Occupation: Select your occupation from the dropdown list.
* Relationship: Select your relationship status from the dropdown list.
* Race: Select your race from the dropdown list.
* Sex: Select your gender from the dropdown list.
* Capital Gain: Enter your capital gain.
* Capital Loss: Enter your capital loss.
* Hours per Week: Slide the hours per week bar to indicate the number of hours you work per week.
* Native Country: Select your native country from the dropdown list.
* After providing the required information, click on the "Predict" button.

The application will process your input and display the prediction result as "Income Level: Greater than 50K" if the model predicts a higher income level or "Income Level: Less than or equal to 50K" if the model predicts a lower income level.
## Web-App:
![image](https://github.com/k-aniket47/Donar-Prediction-Web-App/assets/79148315/b7a0b602-f9b9-4e8e-af72-ac0655726d3a)
![image](https://github.com/k-aniket47/Donar-Prediction-Web-App/assets/79148315/96463605-2289-4f3a-a16d-d1df068594ac)

## Results:
![image](https://github.com/k-aniket47/Donar-Prediction-Web-App/assets/79148315/ff26c5bd-facb-46d6-b9ee-262004efdf9a)
![image](https://github.com/k-aniket47/Donar-Prediction-Web-App/assets/79148315/6fab3a87-0f08-45f1-af89-b278018bf4e4)


## About the Model
The prediction model used in this application is based on XGBoost, a popular machine learning algorithm known for its high performance in tabular data classification tasks. The model was trained on a dataset of income data, and it has learned to identify patterns and make predictions based on the provided input features. The Model Predicts with an accuracy of 87%.

## Purpose
The purpose of this web application is to demonstrate how machine learning algorithms can be utilized to identify potential donors based on their income levels. The application can be used in scenarios where organizations or non-profits are looking to target potential donors for fundraising or charity purposes.

## Disclaimer
This web application and its predictions are provided for demonstration purposes only. The accuracy of the predictions depends on the quality and representation of the training data. The application should not be used for making critical decisions without further validation and analysis.

About
This web application was developed using Streamlit, a powerful Python library for building interactive web applications for data science and machine learning projects.
Feel free to explore and use this web application for predicting donor likelihood based on income level. If you have any questions or feedback, don't hesitate to reach out. Happy predicting! 📈🎉





