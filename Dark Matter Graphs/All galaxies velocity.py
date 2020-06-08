import numpy as np
import matplotlib.pyplot as plt



#Galaxy 1

x1 = np.array([0.7329905,1.1688017,1.4849969,1.883676,2.363244,2.7228281,3.1221209,3.5220268,3.9216874,4.320857,4.6799507,5.040639,5.482584,5.8856797,6.288653,7.0568533,7.9052067,8.752579,9.478863,10.246204,11.13488,11.901854,12.749717,13.557871,14.287344,15.13901,15.950232,16.758877,17.526955,18.254711,19.10331,19.992353,20.84181,21.530594,22.420618,23.109035,23.998323,24.847658,25.576273,26.386023,27.154222,27.964094,28.813921,29.542412,30.432314,31.200884,31.968225,32.817436,33.626205,34.353104,35.20207,35.93142,36.901844])

#Recorded velocity (top crooked curve)
y1 = np.array([44.781902,59.18528,70.86315,80.01302,89.16407,96.17328,104.35038,111.554726,119.14818,127.51984,135.30725,140.56548,145.24123,147.3872,149.72774,150.12807,151.69687,154.82211,157.55647,159.31865,161.08261,163.42845,165.77548,166.95459,164.63058,160.94649,157.26178,157.66269,158.25757,158.65729,159.837,161.0173,160.83514,158.89964,158.52353,157.17169,157.96289,157.97528,157.01314,155.66307,156.06339,154.51877,153.75296,152.98537,152.8038,152.62045,154.38264,154.58958,154.79594,156.55754,157.1536,155.02414,155.4274])

#Predicted velocity from equation (bottem curve)
y2 = np.array([26.86195459,33.60725167,37.93583508,40.00277639,43.70937488,47.8528839,52.48369069,59.80971181,65.64384579,71.31152618,77.87275804,85.10307945,95.79316256,100.0451868,102.9487934,106.745478,107.3854752,106.2992318,104.9927332,104.8584356,103.4263842,102.3589725,100.9223668,99.79374092,98.13715559,96.07871154,93.74746343,91.87761647,90.11456464,88.69925667,87.73905837,87.13439594,86.54058449,85.84586975,83.89642794,82.41186735,81.20218023,81.19961783,81.49184419,81.54124554,81.65007605,81.12519162,80.47813657,79.8451071,79.11677987,78.22440409,77.36686012,76.8723531,76.36207499,76.45566604,76.41244127,76.26322595,76.17717533])

#Sum of Masses (recorded and dark matter) put into Predicted velocity equation (top smooth curve)
y3 = np.array([40.11026427,56.00970012,66.06980768,75.46299586,85.60771275,92.79359028,99.90034912,107.7525381,114.2834396,120.3144645,126.3726673,132.7296911,141.6572987,146.0179582,149.303655,154.0195966,156.3469403,157.1734327,157.447337,158.4185923,158.5433021,158.6575343,158.528321,158.4859514,157.998678,157.312831,156.4063707,155.754682,155.1250673,154.6617975,154.4953385,154.5206249,154.5105767,154.3678285,153.5897759,152.9999715,152.6142508,152.8465576,153.1902718,153.4139108,153.6483675,153.5463451,153.380432,153.1917167,152.9788006,152.6550671,152.3470746,152.233344,152.1005184,152.254243,152.3517288,152.3749777,152.4565072])




#Galaxy 2

x2 = np.array([0.17148362,0.4360183,0.616588,0.8204397,1.0746205,1.2705386,1.5233747,1.722251,1.8940805,2.2038345,2.542518,2.9901965,3.4659977,3.8548758,4.3273153,4.6902223,5.080445,5.497311,5.914312,6.32943,6.744011,7.216719,7.6073456,8.022733,8.493828,8.798068,9.269835,9.687105,10.0485325,10.325861,10.768161,11.294426,11.79324,12.319236,12.762746,13.261829,13.8992405,14.536921,15.091308,15.590391,16.172632,16.75568,17.338459,17.811302,18.311865,18.840012,19.229965,19.508907,19.869797,20.395927,20.921387,21.086357,21.585173,22.056938,22.417292,22.584549,22.971813,23.164639,23.608955,23.996758,24.4147,24.886467,25.330648,25.693153,25.861082])

#Recorded velocity (top curve crooked)
y4 = np.array([17.194363,37.724133,57.156334,70.53634,76.94638,79.50738,84.0837,90.6789,98.19186,104.7835,113.024605,118.69494,124.9145,126.00228,127.63752,131.11005,134.03156,135.4852,137.12221,136.192,134.5283,136.53029,140.0019,139.43845,139.23996,138.31331,139.03168,141.03543,142.49086,142.66533,141.00075,140.43373,140.23434,139.30057,139.28635,139.4537,139.24986,139.41278,139.39499,139.56235,139.72705,140.99197,141.89017,144.07552,146.25998,148.26018,150.81494,153.1899,153.91183,153.16144,151.49417,149.6551,149.45572,150.1741,150.16254,151.44081,150.32811,148.67152,149.75754,149.37834,152.29897,153.01733,153.91997,156.84236,159.0375])

#Predicted velocity from equation (Bottem curve)
y5 = np.array([18.4668304,39.22330349,45.74012225,55.41912981,66.94461967,73.58686263,81.79090837,88.82384037,93.24689908,101.4989852,108.3382821,114.0167293,118.4020753,119.4906759,119.2045895,117.2689789,115.2744814,112.9153218,111.1748553,109.9668863,108.9009241,107.7907853,106.8546286,105.5856082,103.8418217,102.7465969,101.0205122,99.71516986,98.34156755,97.22635829,95.83571242,94.58800742,93.35049171,92.47522197,92.32566093,91.99257374,90.37340727,88.86968551,88.35803883,88.66008721,88.11204912,87.8893893,88.10512033,88.03166384,87.89534756,87.96167471,87.57739863,87.20217276,86.78149643,86.63382756,85.29834842,84.84393508,83.73900431,83.07364142,82.28676825,81.98150171,80.94138172,80.48856286,79.84171698,78.85380949,78.06324152,77.31978789,76.52804614,76.20619253,76.17695269])

#Sum of Masses (recorded and dark matter) put into Predicted velocity equation (top smooth curve)
y6 = np.array([19.84249989,43.2451128,52.30165571,64.50136719,78.91126108,87.82614028,98.63635688,107.3076719,113.2225862,123.6696436,132.7242081,141.2006633,148.138053,151.3780686,153.6545276,153.8567482,153.9864233,153.8067392,153.9493921,154.3467576,154.7325372,155.1286483,155.3609844,155.3519424,155.0665963,154.8708316,154.505587,154.2876216,153.9159423,153.5787943,153.2641679,153.1064567,152.8878997,152.8853577,153.2108299,153.4479533,153.0022113,152.5984959,152.6878168,153.1883642,153.228331,153.4341111,153.8697593,154.0666046,154.2289474,154.506899,154.4578974,154.3628435,154.2730002,154.3960284,153.8474386,153.6558966,153.2251153,153.0227782,152.7153968,152.6048876,152.1706658,151.9896665,151.7816566,151.3773524,151.0852879,150.831671,150.5450058,150.4748513,150.5023644])





#Galaxy 3

x3 = np.array([0.247557,0.37785017,0.5081433,0.78175896,0.93811077,1.0814332,1.3289902,1.4723127,1.6026058,1.8762215,2.0065145,2.2801304,2.553746,2.8273616,3.1009772,3.3615634,3.6482084,3.9218242,4.1824102,4.442997,4.729642,4.990228,5.1465797,5.2638435,5.394137,5.680782,5.8241043,5.954397,6.214984,6.501629,6.775244,6.9055376,7.04886,7.3094463,7.452769,7.5830617,7.726384,7.830619,8,8.130293,8.260587])

#Measured velocity (top curve crooked)
y7 = np.array([9.565217,13.652174,16.26087,18.173914,20.347826,22.695652,26.173914,28,30.26087,33.304348,34.52174,35.217392,36.608696,37.739132,39.130436,40.173912,41.304348,43.130436,44.434784,45.826088,47.304348,48.52174,47.913044,47.47826,48.086956,47.826088,48.434784,48.347828,47.391304,46.608696,47.826088,47.913044,47.130436,48.086956,48.52174,50.086956,51.391304,50.434784,51.826088,52.695652,53.304348])

#Predicted velocity from equation (Bottem curve)
y8 = np.array([6.771713658,10.39767454,12.54577799,15.83726615,17.36681243,18.78002597,20.66618459,21.41332087,22.03739013,24.22212027,24.71357117,25.35896795,25.49406158,25.7210195,25.93318216,25.81561265,25.71436706,25.7553736,25.73142565,25.74788161,25.70912517,25.84192637,25.83736772,25.84993142,25.87693796,25.58811063,25.34424056,25.19473366,24.88431773,24.70722592,24.12439471,23.88268868,23.85698773,23.65278294,23.32551515,23.0259596,22.79919544,22.63481779,22.33383084,22.07043761,21.91944853])

#Sum of Masses (recorded and dark matter) put into Predicted velocity equation (top smooth curve)
y9 = np.array([12.45367697,18.95114844,24.55405262,35.3393588,41.02948612,46.0085988,53.80623496,57.85503328,61.3101927,68.26187694,71.10269106,76.42656116,80.97302135,85.02382572,88.61539022,91.5804801,94.50146761,97.03175304,99.1922317,101.1655104,103.1222994,104.7838768,105.6948744,106.3526161,107.0587568,108.4341336,109.0543553,109.6116413,110.661162,111.7642023,112.6496663,113.0558262,113.536576,114.3346612,114.7077392,115.0347665,115.4025121,115.6619906,116.0632863,116.3549431,116.6587422])





plt.plot(x1,y1,'-')
#plt.plot(x1,y2,'-')
#plt.plot(x1,y3, '-')

plt.plot(x2,y4,'-')
#plt.plot(x2,y5,'-')
#plt.plot(x2,y6, '-')

plt.plot(x3,y7,'-')
#plt.plot(x3,y8,'-')
#plt.plot(x3,y9, '-')





plt.title('Galaxies 1,2,3 - measured velocity', fontsize=20)
plt.xlabel('Radius (kpc)',fontsize=15)
plt.ylabel('Velocity (km/s)', fontsize=15)
plt.axis([0,40,0,170])
plt.legend(['Galaxy 1','Galaxy 2','Galaxy 3'])
plt.show()