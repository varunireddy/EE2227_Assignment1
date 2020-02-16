import numpy as np
import matplotlib.pyplot as plt
import math as mp
from pylab import *
import cmath
m = np.array([])
w = np.linspace(0,1000,10001)
h_w = 100/((0+1j)*w+30)
#h_w = 10*((0+1j)*w+100)/((0+1j)*w+1)
h = abs(h_w)
phase = np.array([])
for i in h:
	m = np.append(m,[20*mp.log(i)/mp.log(10)])
for k in h_w:
	phase = np.append(phase,[(np.degrees(cmath.phase(k)))])	
plt.grid()
plt.semilogx(w,m)
plt.title("magnitude plot")
figure(2)
plt.semilogx(w,phase)
plt.grid()
plt.title("phase plot")
plt.show()
