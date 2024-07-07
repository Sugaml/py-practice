import numpy as np 
import matplotlib as plt

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y)
plt.title("Plot 1")
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.title("Plot 2")
plt.subplots_adjust(left = 0.1,
bottom = 0.1,
right = 0.9,
top = 0.9,
wspace = 0.4,
hspace = 0.4)
plt.show()