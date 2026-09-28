import numpy as np
import matplotlib.pyplot as plt

try:
    logo=np.load('numpy-logo.npy')

    #Display
    plt.figure(figsize=(10,5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("Numpy logo")
    plt.grid(False)

    dark_logo=1-logo
    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("Numpy Dark_logo")
    plt.grid(False)
    plt.show()

except FileNotFoundError:
    print("Logo not found!")