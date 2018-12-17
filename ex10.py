import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = (np.sin(x - 2) **2) * np.exp(-x **2)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel('X')
plt.ylabel('F(X)')
plt.title('Exercise 10')
