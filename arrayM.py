import numpy as np

print("Intermediate 1")
arr=np.array([
    [10,20,30,40],
 [50,60,70,80],
 [90,100,110,120]
 ])
print("\nMatrix:")
print(arr)
print("\nDimension:",arr.ndim ,"\nRows:",arr.shape[0], "\nColumn:",arr.shape[1],"\nTotal elements:",arr.size ,"\nDatatype:",arr.dtype)

print("Intermediate 2")
print("\nOrignal Array")
m=np.arange(1,13)
print(m)
print("Reshaped Array")
reshape=m.reshape(3,4)
print(reshape)
transpose=reshape.T
print("\nTranspose:")
print(transpose)