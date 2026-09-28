import numpy as np 

vector1=np.array([1,2,3,4,5])
vector2=np.array([6,7,8,9,10])
print("Vector Addintion:",vector1+vector2)
print("Vector Multiplication:",vector1*vector2)
print("Vector Dot product:",np.dot(vector1,vector2))
angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print(angle)

restaurant_types = np.array(
    [
     'biryani', 
     'chinese', 
     'pizza',
     'burger', 
     'cafe'
     ]
)
vectorized_upper=np.vectorize(str.upper)
print(vectorized_upper(restaurant_types))