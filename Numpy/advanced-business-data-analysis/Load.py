import numpy as np
import matplotlib.pyplot as plt

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.random.rand(3, 3)
array3 = np.zeros((4, 4))

#Saving arrays in a file 
np.save('array1.npy',array1)
np.save('array2.npy',array2)
np.save('array3.npy',array3)

#Loading array
loaded_array1=np.load('array1.npy')
print(loaded_array1) 