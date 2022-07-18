import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

''' 1. Importing the dataset '''

dataset = pd.read_csv("./Dataset/Salary_Data.csv")
# dataset.head()  -- This shows the first few columns of our dataset
print(dataset)

''' 2. Data Preprocessing'''

x = dataset.iloc[:, :-1].values  # independent variable array
print("x-axis values: ", x)
y = dataset.iloc[:, 1].values  # dependent variable vector
print("y-axis values: ", y)

''' 3. Splitting the dataset to train 
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=0)  # Split arrays or matrices
# into random train and test subsets.
print(f"x_train: {x_train}\nx_test: {x_test}\nY_train: {y_train}\ny_test: {y_test}")

''' 3. Fitting linear regression model into the training set '''

regressor = LinearRegression()
linear_equation = regressor.fit(x_train, y_train)  # actually produces the linear eqn for the data
print(f"Linear Equation: {linear_equation}")

''' 5. Predicting the test set results '''

y_pred = regressor.predict(x_test)  # predict method makes the predictions for the test set
print(f"The predicted salaries of the test set are: {y_pred}")
print(f"The real salaries of the test set are {y_test}")

''' 6. Visualizing the results '''
"""6.1  Plotting the points (observations)"""
"""6.2  Plotting the regression line"""

# plot for the TRAIN dataset

plt.scatter(x_train, y_train, color='red')  # plotting the observation line
plt.plot(x_train, regressor.predict(x_train), color='blue')  # plotting the regression line
plt.title("Salary vs Experience (Training set)")  # stating the title of the graph
plt.xlabel("Years of experience")  # adding the name of x-axis
plt.ylabel("Salaries")  # adding the name of y-axis
plt.show()  # specifies end of graph

# plot for the TEST dataset

plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')  # plotting the regression line
plt.title("Salary vs Experience (Testing set)")
plt.xlabel("Years of experience")
plt.ylabel("Salaries")
plt.show()
