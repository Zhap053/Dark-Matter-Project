import numpy as np
import matplotlib.pyplot as plt

x = np.array([])

#Recorded velocity (bottem curve)
y1 = np.array([])

#Predicted velocity from equation (top crooked curve)
y2 = np.array([])

#Sum of Masses (recorded and dark matter) put into Predicted velocity equation (top smooth curve)
y3 = np.array([])

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.xlabel('Radius (kpc)')
plt.ylabel('Velocity (km/s)')
plt.axis([0,40,0,180])
plt.show()
