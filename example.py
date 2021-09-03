from control.matlab import *
import matplotlib.pyplot as plt


s = tf('s')
G = 1/(s+1)
[y,t]=step(G)

plt.plot(t,y)
plt.grid()
plt.show()
