import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cl

N = 255

colors = [[k/255.0, (255.0-k)/255.0, 1.0] for k in range(255)]
cm = cl.ListedColormap(colors, name='my_color_map', N=N)

n = 120
x = np.arange(-1, 1, 1.0/n)
y = np.arange(-1, 1, 1.0/n)
X, Y = np.meshgrid(x, y)
z = np.cos(X)+np.sin(10*Y)

plt.plot(1, 1, 0)
plt.pcolor(x, y, z, cmap='jet')
plt.colorbar()

plt.title('График')
plt.grid(True)
plt.show()
