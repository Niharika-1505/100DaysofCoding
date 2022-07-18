import numpy as np
from numpy import cov

# https://www.tutorialandexample.com/covariance-in-python#

x = np.array([2, 3, 2.7, 3.2, 4.1])
y = np.array([10, 14, 12, 15, 20])

covariance = np.cov(x, y)[0][1]
print(f"covariance of x:{x} and y:{y} is: {covariance}")

a = np.array([2, 4, 1, 6, 2, 1, 7, 5, 8])
b = np.array([7, 2, 3, 1, 8, 6, 2, 3, 4])
sigma = cov(a, b)[0, 1]
print(f"covariance of a:{a} and b:{b} is: {sigma}")
