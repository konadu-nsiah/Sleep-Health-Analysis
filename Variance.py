import numpy as np
import math
x =np.array([1,3,5,6])
Varriance = np.var(x)
mean= np.mean(x)
print(mean)
print(Varriance)


# Covariance calculation
x =np.array([1,3,5,6])
y = np.array([-2,-4,-5,-6])
cov_xy=np.cov(x,y)
print(cov_xy)


# Correlation coefficient
corr=np.corrcoef(x,y)
print(corr)