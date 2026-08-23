import numpy as np

print("Practice 1:")
arr=np.array([10,20,30,40,50])
print("Array:",arr , "\nType:",type(arr) , "\nDimension:",arr.ndim , "\nShape:",arr.shape ,"\nSize:",arr.size ,"\nDatatype:",arr.dtype)

print("Practice 2:")
v=np.array([1,2,3,4,5,6])
print("Before Reshape:",v)
print("Dimension:",v.ndim , "\nShape:",v.shape ,"\nSize:",v.size)
v=v.reshape(2,3)
print("After Reshape")
print(v)
print("Dimension:",v.ndim , "\nShape:",v.shape ,"\nSize:",v.size)
