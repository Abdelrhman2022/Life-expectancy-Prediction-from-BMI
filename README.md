# Life expectancy Prediction from BMI
Explore and run machine learning code with data on the average life expectancy at birth and the average BMI for males across the world. The data comes from 
<a herf= 'https://www.gapminder.org/'> Gapminder </a>

# Dataset
The data file can be found under the "bmi_and_life_expectancy.csv". It includes three columns, containing the following data:

* Country – The country the person was born in.
* Life expectancy – The average life expectancy at birth for a person in that country.
* BMI – The mean BMI of males in that country.

# Load the data

The data is in the file called "bmi_and_life_expectancy.csv".
Use pandas read_csv to load the data into a dataframe (don't forget to import pandas!)
Assign the dataframe to the variable bmi_life_data.

# Build a linear regression model

Create a regression model using scikit-learn's LinearRegression and assign it to bmi_life_model.
Fit the model to the data.

# Predict using the model

Predict using a BMI of 21.07931 and assign it to the variable laos_life_exp.
