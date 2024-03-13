# before doing iccfcut, please make sure the host component has been removed.
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import interpolate
import argparse, sys

contf=sys.argv[1] # continuum band lightcurve
linef=sys.argv[2] # line band lightcurve
ratio=float(sys.argv[3]) # Ha ratio in the line band, determined from the spectrum

a1=np.loadtxt(contf).T
a2=np.loadtxt(linef).T

x1,y1,dy1=a1[0],a1[1],a1[2]
x2,y2,dy2=a2[0],a2[1],a2[2]
f=interpolate.interp1d(x1,y1,kind='slinear')
f2=interpolate.interp1d(x1,dy1,kind='slinear')

fname='Halpha.txt' # file name of the extracted emission line 
f3=open(fname,'a+')
f3.seek(0)
f3.truncate()

# define the ratio of continuum component in the line band
def define_alpha(fx1,fy1,fx2,fy2):
    alpha=[]
    flag=0
    for i in range(len(fx2)):
        lena=len(alpha)
        if fx2[i]>min(fx1) and fx2[i]<max(fx1):
            for j in range(flag,len(fx1)):
                if abs(fx2[i]-fx1[j])<5:
                    alpha.append((1-ratio)*fy2[i]/f(fx2[i]))
                    flag=j
                    break
        if len(alpha)==lena:
            alpha.append(100)  # just a number large enough
    alphan=np.min(alpha)
    return alphan

# devide the lightcurves into different seasons and calculate the ratio for each season
gap=[58000,58450,58800,59150,59500,60000] # each value corresponds to the end of each season (or the start of the next season)
for p in range(len(gap)-1):
    select1=(x1>gap[p]) & (x1<gap[p+1])
    x1c,y1c,dy1c=x1[select1],y1[select1],dy1[select1]
    select2=(x2>gap[p]) & (x2<gap[p+1])
    x2c,y2c,dy2c=x2[select2],y2[select2],dy2[select2]
    a=define_alpha(x1c,y1c,x2c,y2c)
    for i in range(len(x2c)):
        if x2c[i]>min(x1c) and x2c[i]<max(x1c) :
            for j in range(len(x1c)):
                if abs(x2c[i]-x1c[j])<5:
                    fgr=y2c[i]-f(x2c[i])*a
                    dgr=dy2c[i]+f2(x2c[i])*a
                    result=str(x2c[i])+'\t'+str(fgr)+'\t'+str(dgr)+'\n'
                    f3.write(result)
                    break
f3.close()

# plot 3 lightcurves (continuum band, line band, Halpha)

a3=np.loadtxt(fname).T
x3,y3,dy3=a3[0],a3[1],a3[2]

plt.rcParams['font.size'] = 18
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['figure.titlesize'] = 18
plt.rcParams['xtick.direction'] = 'in' 
plt.rcParams['ytick.direction'] = 'in' 

plt.figure()
plt.errorbar(x1,y1,yerr=dy1,fmt='.',c='r')
plt.errorbar(x2,y2,yerr=dy2,fmt='.',c='b')
plt.errorbar(x3,y3,yerr=dy3,fmt='.',c='black')
plt.legend(labels=['g','r','Ha'],frameon=1)

plt.xlabel('MJD/day')
plt.ylabel('Normalized flux')
plt.tick_params(top=True, right=True, which='both')

plt.tight_layout()
plt.savefig('lightcurve')
