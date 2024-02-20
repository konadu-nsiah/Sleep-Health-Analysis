import numpy as np
import matplotlib.pyplot as plt
# Binomial distribution describes the distribution of binary data from a finite sample. Thus

#it gives the probability of getting r events out of n trials.
n= 8
lambda_=7
p = 0.16
N =1000
X =np.random.binomial(n,p,N)
counts, bins, ignored = plt.hist(X, 20, density= True, rwidth=0.7,color ="Purple")
plt.title("Binomial distribution with p=0.16 n=8")
plt.ylabel("Probability")
plt.xlabel("Number of Successes")
plt.show()
#Poisson distribution describes the distribution of binary data from an infinite sample. Thus
# it gives the probability of getting r events in a population. 
Y=np.random.poisson(lambda_,N)
counts, bins, ignored = plt.hist(Y, 50, density= True, rwidth=0.7,color ="Pink")
plt.title("Randomly generating from Poisson Distribution with lambda=7")
plt.ylabel("Probability")
plt.xlabel("Number of Visitors")
plt.show()