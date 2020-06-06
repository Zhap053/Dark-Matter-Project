import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.17148362,0.4360183,0.616588,0.8204397,1.0746205,1.2705386,1.5233747,1.722251,1.8940805,2.2038345,2.542518,2.9901965,3.4659977,3.8548758,4.3273153,4.6902223,5.080445,5.497311,5.914312,6.32943,6.744011,7.216719,7.6073456,8.022733,8.493828,8.798068,9.269835,9.687105,10.0485325,10.325861,10.768161,11.294426,11.79324,12.319236,12.762746,13.261829,13.8992405,14.536921,15.091308,15.590391,16.172632,16.75568,17.338459,17.811302,18.311865,18.840012,19.229965,19.508907,19.869797,20.395927,20.921387,21.086357,21.585173,22.056938,22.417292,22.584549,22.971813,23.164639,23.608955,23.996758,24.4147,24.886467,25.330648,25.693153,25.861082])

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