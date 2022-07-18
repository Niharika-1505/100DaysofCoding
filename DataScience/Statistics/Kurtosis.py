import scipy.stats as sps
import numpy as np

data = np.array([88, 85, 82, 97, 67, 77, 74, 86, 81, 95, 77, 88, 85, 76, 81])
kurtosis = sps.kurtosis(data, bias=False)
print(kurtosis)

