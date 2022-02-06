# import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression


#Load the data
bmi_life_data = pd.read_csv("bmi_and_life_expectancy.csv") 
x_values = bmi_life_data[["BMI"]]
y_values = bmi_life_data[["Life expectancy"]]
# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model


bmi_life_model = LinearRegression()

#Predict life expectancy for a BMI value of 20.0123
bmi_life_model.fit(x_values, y_values)
laos_life_exp = bmi_life_model.predict(20.0123)
print(laos_life_exp)