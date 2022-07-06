import numpy as np

x = np.array([41, 19, 23, 40, 55, 57, 33])
y = np.array([94, 60, 74, 71, 82, 76, 61])

correlationCoefficient = np.corrcoef(x, y)[0][1]
print(f"correlation coefficient of x:{x} and y:{y} is: {correlationCoefficient}")
