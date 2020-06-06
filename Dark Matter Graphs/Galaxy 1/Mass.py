import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.7329905,1.1688017,1.4849969,1.883676,2.363244,2.7228281,3.1221209,3.5220268,3.9216874,4.320857,4.6799507,5.040639,5.482584,5.8856797,6.288653,7.0568533,7.9052067,8.752579,9.478863,10.246204,11.13488,11.901854,12.749717,13.557871,14.287344,15.13901,15.950232,16.758877,17.526955,18.254711,19.10331,19.992353,20.84181,21.530594,22.420618,23.109035,23.998323,24.847658,25.576273,26.386023,27.154222,27.964094,28.813921,29.542412,30.432314,31.200884,31.968225,32.817436,33.626205,34.353104,35.20207,35.93142,36.901844])

#Measured mass (bottem curve)
y1 = np.array([123000000.00,307000000.00,497000000.00,701000000.00,1050000000.00,1450000000.00,2000000000.00,2930000000.00,3930000000.00,5110000000.00,6600000000.00,8490000000.00,11700000000.00,13700000000.00,15500000000.00,18700000000.00,21200000000.00,23000000000.00,24300000000.00,26200000000.00,27700000000.00,29000000000.00,30200000000.00,31400000000.00,32000000000.00,32500000000.00,32600000000.00,32900000000.00,33100000000.00,33400000000.00,34200000000.00,35300000000.00,36300000000.00,36900000000.00,36700000000.00,36500000000.00,36800000000.00,38100000000.00,39500000000.00,40800000000.00,42100000000.00,42800000000.00,43400000000.00,43800000000.00,44300000000.00,44400000000.00,44500000000.00,45100000000.00,45600000000.00,46700000000.00,47800000000.00,48600000000.00,49800000000.00])

#Dark Matter Mass (middle curve)
y2 = np.array([151246401.17,545705126.24,1010520326.78,1793628237.93,2977781436.79,4002400200.32,5246282694.23,6579971556.27,7981628037.88,9435783608.99,10781174782.39,12161581078.91,13885549591.43,15483724129.13,17101681943.70,20230913729.60,23739014873.37,27283541844.57,30346006572.51,33600779157.29,37389792044.85,40673489829.06,44315360896.51,47796243869.14,50944950499.47,54627913418.90,58141807543.40,61649378613.63,64984861162.32,68148289595.76,71840295226.20,75711601376.43,79413333172.37,82416675928.02,86299610830.51,89304464766.29,93187806988.49,96898309293.89,100082565701.39,103622534754.82,106981862383.58,110524396632.87,114242683446.10,117430819332.40,121326194730.10,124691155560.46,128051327940.65,131770647641.11,135313422379.70,138498019103.74,142217902704.34,145414074008.26,149667224463.42])

#Sum of Masses
y3 = np.array([274246401.17,852705126.24,1507520326.78,2494628237.93,4027781436.79,5452400200.32,7246282694.23,9509971556.27,11911628037.88,14545783608.99,17381174782.39,20651581078.91,25585549591.43,29183724129.13,32601681943.70,38930913729.60,44939014873.37,50283541844.57,54646006572.51,59800779157.29,65089792044.85,69673489829.06,74515360896.51,79196243869.14,82944950499.47,87127913418.90,90741807543.40,94549378613.63,98084861162.32,101548289595.76,106040295226.20,111011601376.43,115713333172.37,119316675928.02,122999610830.51,125804464766.29,129987806988.49,134998309293.89,139582565701.39,144422534754.82,149081862383.58,153324396632.87,157642683446.10,161230819332.40,165626194730.10,169091155560.46,172551327940.65,176870647641.11,180913422379.70,185198019103.74,190017902704.34,194014074008.26,199467224463.42])

plt.plot(x,y1,'y--')
plt.plot(x,y2,'--')
plt.plot(x,y3, 'g')

plt.title('Galaxy 1', fontsize=25)
plt.xlabel('Radius (kpc)',fontsize=15)
plt.ylabel('Mass (solar masses)', fontsize=15)
plt.axis([0,40,0,210000000000])
plt.legend(['Visable Mass','Dark Matter Mass','Added Mass '])
plt.show()