import math
import numpy as np
import matplotlib.pyplot as plt


def normal_dist(data_vector, x):
    n = data_vector.shape[0]

    mean = np.sum(data_vector) / n

    std_dev = math.sqrt(np.sum((data_vector - mean) ** 2) / n)

    return math.exp(-1 / 2 * ((x - mean) / std_dev) ** 2) \
           / (std_dev * math.sqrt(2 * math.pi)) 





arr = np.array([4, -9, 1, -2, -5, 12])


x_values = []
y_values = []


for x in range(-50, 51):
    x_values.append(x)
    y_values.append(normal_dist(arr, x))

plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-60, 60, 0, 0.1])
plt.plot(x_values, y_values)
plt.show()