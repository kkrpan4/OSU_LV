import numpy as np 
import matplotlib.pyplot as plt


x = np.array([1.0, 2.0, 3.0, 3.0, 1.0])
y = np.array([1.0, 2.0, 2.0, 1.0, 1.0])

plt.axis([0.0, 4.0, 0.0, 4.0])

plt.plot(x, y, color = 'red', marker = 'o', linewidth = 5, markersize = 10)
plt.show()
