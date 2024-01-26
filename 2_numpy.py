'''
Neural Network Deep Learning
ICP 3
author: Madhulika Dayal
student ID: 700743206
email: mxd32060@ucmo.edu

2. Numpy
Using NumPy create random vector of size 20 having only float in the range 1-20.
Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1)
(you can NOT implement it via for loop)
'''
import numpy as np

# created a random vector of size 20 with float values between 1 and 20
ranvec = np.random.uniform(low=1, high=20, size=20)
print(ranvec)
# reshape the array to 4 by 5 using reshape method
mat45 = ranvec.reshape(4, 5)
print(mat45)
# replace the max in each row by 0 using where method
mat45 = np.where(mat45 == np.amax(mat45, axis=1, keepdims=True), 0, mat45)
print(mat45)