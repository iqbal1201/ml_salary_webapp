## Machine Learning Salary Predictor ( Deployed on Web App Streamlit & Docker)


### Introduction
In today's data-driven world, organizations are constantly seeking ways to make informed decisions based on data analysis. One area where data analysis plays a crucial role is in predicting salary. Salary prediction models can provide valuable insights for job seekers, employers, and policymakers alike.

The goal of this project is to create a simple machine learning model to predict salary based on several key features: education level, country, and years of experience. The project utilizes data collected from the Stack Overflow Developer Survey in 2022, a widely recognized source of information in the software development community. The project also aims to make the model accessible through a user-friendly interface built with Streamlit and containerized using Docker for easy deployment and sharing.

### Data Collection
#### Stack Overflow Developer Survey 2022
The dataset used for this project is derived from the Stack Overflow Developer Survey 2022, which is an annual survey conducted by Stack Overflow, one of the largest online communities for programmers. The survey collects a wide range of information about developers, including their demographics, education, job preferences, and, most importantly for this project, salary information.

Key features from the survey data include:

Education level: This feature represents the highest level of education achieved by the survey respondents. It can range from high school to doctoral degrees.
Country: The country in which the survey respondents are located. This provides geographical context, as salaries can vary significantly by country.
Years of experience: The number of years of professional programming experience.
Data Preprocessing
Before building the machine learning model, the dataset undergoes preprocessing to ensure it is suitable for analysis:

Handling missing values: Any missing values in the dataset are addressed using appropriate techniques, such as imputation or removal of rows/columns.
Encoding categorical variables: Categorical variables like education level and country are encoded into numerical values using techniques like one-hot encoding.
Feature scaling: Numerical features like years of experience are scaled to have similar ranges to prevent some features from dominating the model.

### Machine Learning Model
#### Model Selection
For salary prediction, a regression model is chosen. Regression models are suitable for predicting continuous numerical values, making them ideal for predicting salaries.

Common regression models that can be considered for this task include:

Linear Regression
Decision Tree Regression
Random Forest Regression
Gradient Boosting Regression
The choice of the specific model depends on the data and performance during model evaluation.

#### Model Evaluation
The model's performance is evaluated using standard regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) score. Cross-validation techniques may be employed to ensure the model's generalizability.

### Deployment with Streamlit and Docker
#### Streamlit
Streamlit is an open-source Python library that allows for easy creation of web applications for data science and machine learning. In this project, Streamlit is used to create a user-friendly web interface where users can input their education level, country, and years of experience, and the model will predict their estimated salary. The Streamlit app provides an intuitive way to interact with the machine learning model.

#### Docker
Docker is a platform for developing, shipping, and running applications in containers. Docker containers provide a consistent environment, making it easy to package the application, its dependencies, and even the machine learning model into a single deployable unit. This simplifies deployment and ensures that the application runs consistently across different environments.

By containerizing the Streamlit app and its associated components, such as the machine learning model and data preprocessing scripts, users can easily deploy the entire application in a Docker container, making it accessible and shareable with others.

### Conclusion
The project's goal is to leverage machine learning to predict salaries based on education level, country, and years of experience using data from the Stack Overflow Developer Survey 2022. The project combines data preprocessing, model development, and user interface creation with Streamlit for a seamless user experience. Docker containerization ensures that the application can be easily shared and deployed on various platforms, making it accessible to a wider audience.

Predicting salaries can have practical applications for job seekers, employers, and policymakers, providing valuable insights into compensation trends and helping individuals make informed career decisions.



### Result
See the the image below for the web-app
![image](https://github.com/iqbal1201/ml_salary_webapp/assets/70199329/1f007dbd-735e-45e0-9608-ff64bef0b3cf)

See the the image below for the web-app

![image](https://github.com/iqbal1201/ml_salary_webapp/assets/70199329/92282388-05da-4d9a-860f-9011d8ade607)

