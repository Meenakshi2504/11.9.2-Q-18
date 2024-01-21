import matplotlib.pyplot as plt
import numpy as np

a = 120
d = 5
start_n = -5
end_n = 10

x = np.arange(start_n, end_n + 1, 1)
y = a + x*d
y[x<0]=0

# Use plt.plot for markers with smaller size
plt.plot(x, y, 'ro-', markersize=5, linewidth=0)
# Use plt.stem for the stem plot
plt.stem(x, y, basefmt='b-', linefmt='-', markerfmt=' ')
plt.title('General Term of Arithmetic Progression')
plt.xlabel('n')
plt.ylabel('Term Value')
plt.grid(True)
plt.savefig('./figs/python.1(1).png')
plt.show()

