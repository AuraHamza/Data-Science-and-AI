import numpy as np
tensor=np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],

    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("Orginal Tensor:")
print(tensor)

print("\nDimension:",tensor.ndim , "\nShape:",tensor.shape, "\nTotal Elements:",tensor.size)
print("\nTranspose:")
print(tensor.T)


print("\n Final Task\n")
arr=np.arange(1,25)
print(arr)

re=arr.reshape(4,6)
print("\nReshaped 4x6:")
print(re)

tran=re.T
print("\nTransposed:")
print(tran)

flat=tran.flatten()
print("\nFlattened:")
print(flat)

ravelled=tran.ravel()
print("\nRaveled:")
print(ravelled)

print("\nMaking changes")

flat=arr.flatten()
print("\nFlattened:")
print(flat)

ravelled=arr.ravel()
print("\nRaveled:")
print(ravelled)

flat[0]=999
print("\nFlattend: ",flat)
print("Orignal Array: ")
print (arr)

ravelled[0]=888
print("\nraveled: ",ravelled)
print("Orignal Array: ")
print (arr)

