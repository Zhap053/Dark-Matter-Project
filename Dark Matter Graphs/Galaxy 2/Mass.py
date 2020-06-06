import numpy as np
import matplotlib.pyplot as plt

x = np.array([])

#Measured mass (bottem curve)
y1 = np.array([])

#Dark Matter Mass (middle curve)
y2 = np.array([])

#Sum of Masses
y3 = np.array([])

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xlabel('Radius (kpc)')
plt.ylabel('Mass (Solar masses)')
plt.axis([0,40,122000000,210000000000])
plt.show()