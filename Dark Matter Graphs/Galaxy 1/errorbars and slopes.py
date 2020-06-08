import numpy as np
import matplotlib.pyplot as plt
x=np.array([5,10,15,20,25])
y=np.array([0.2,0.5,0.8,1.0,1.3])
yerror = np.array([0.05,0.05,0.05,0.05,0.05])

#where we make some initial guess of
#what the slope of the line will be
fx_estimate=0.05*x
print("My estimate best fit gradient is: 0.05\n")

#print(fx)  #shows every fx value


count = 0
minchi2=10000
minslope=0.0
start =0
stop = 0.1
step =0.0001	 

chi2=(y-fx_estimate)*(y-fx_estimate)/np.power(yerror,2)
#print(chi2.sum())	#shows every chi value

for slope in np.arange(start, stop, step):
      fx=slope*x
      chi2=np.sum(((y-fx)*(y-fx))/np.power(yerror,2))
      if(chi2<minchi2):
          minchi2=chi2
          minslope=slope
      #print(slope,chi2,minslope,minchi2)
print('The optimised bestfit graident is: ',minslope) #prints optimised graident for best fit
fx_optimised=minslope*x

plt.errorbar(x,y,yerror,fmt='bs--') 
plt.plot(x,fx_estimate,'r-')  
plt.plot(x,fx_optimised,'g-')   
plt.legend(['Estimated Line of Best Fit','Optimised Line of Best Fit']) 
plt.show()