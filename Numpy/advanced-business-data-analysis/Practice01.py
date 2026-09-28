
import numpy as np 
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub  
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])
print("====PandaMart Sales analysis===")
print("Sales data Shape:",sales_data.shape)
print("Sample data for 1st 3 restau:", sales_data[:3])
# print with out id 
# print("Sample data for 1st 3 restau:", sales_data[:,1:])
print("\nTotal sale per year:")
print(np.sum(sales_data,axis=0))#id bhi include ho rahi ha
print(np.sum(sales_data[:,1:],axis=0))#is ma nhi ho raha
#axis=1 => row 
#axis=0 =>col
print("\nMinimum Sales Per Resturant:")
print(np.min(sales_data[:,1:],axis=1))

print("\nMax sale per year:")
print(np.max(sales_data[:,1:],axis=0))

print("\nAverage Sale per Resturant:")
print(np.average(sales_data[:,1:],axis=1))

print("\nCumulative Sales: ")
print(np.cumsum(sales_data[:,1:],axis=1))
cusum=np.cumsum(sales_data[:,1:],axis=1)


# Broadcasting Vectorized 
monthly_avg=sales_data[:,1:]/12
print("\nMonthly_avg:")
print(np.trunc(monthly_avg))

plt.figure(figsize=(10,6))
plt.plot(np.mean(cusum,axis=0),marker='o')
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.show()