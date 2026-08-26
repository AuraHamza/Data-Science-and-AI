import numpy as np

print("\nPractice 1:")
arr=np.array([10,20,30,40,50])
print("\nArray:",arr , "\nType:",type(arr) , "\nDimension:",arr.ndim , "\nShape:",arr.shape ,"\nSize:",arr.size ,"\nDatatype:",arr.dtype)

print("\nPractice 2:")
v=np.array([1,2,3,4,5,6])
print("\nBefore Reshape:",v)
print("Dimension:",v.ndim , "\nShape:",v.shape ,"\nSize:",v.size)
v=v.reshape(2,3)
print("After Reshape")
print(v)
print("Dimension:",v.ndim , "\nShape:",v.shape ,"\nSize:",v.size)

print("\nFlatten vs Ravel")
m=np.array([
    [1,2,3],
    [4,5,6]
])
print("\n2d array:")
print(m)
flattened = m.flatten();
print("flattened:",flattened)
raveled = m.ravel()
print("ravelled:",raveled)

print("\nMaking changes")
flattened[0]=100
print("\nFlattend: ",flattened)
print("Orignal Array: ")
print (m)

raveled[0]=200
print("\nraveled: ",raveled)
print("Orignal Array: ")
print (m)