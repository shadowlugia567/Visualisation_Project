import matplotlib.pyplot as plt 
import numpy as np 

import math as m
print("Welcome!")

u = float(input("Please enter the intial velocity(in metres/second):"))
A = float(input("Please enter in the angle at which it was launched(in radians between 0 and pi/2):"))
time = (2*u*m.sin(A))/9.8 

print("Time taken is",time,"s")

x = np.arange(0, time, 0.01) 

y = x*u*np.cos(A)

a = (-9.8/2)*x*x + (u*np.sin(A))*x 

plt.figure(1)
plt.plot(x, y)
plt.figure(1).suptitle('Range vs Time Graph', fontsize=20)
plt.xlabel('Time (seconds)', fontsize=16)
plt.ylabel('Range (metres)', fontsize=16)

plt.figure(2)
plt.plot(x, a)
plt.figure(2).suptitle('Height vs Time Graph', fontsize=20)
plt.xlabel('Time (seconds)', fontsize=16)
plt.ylabel('Height (metres)', fontsize=16)

plt.figure(3)
plt.plot(y, a)
plt.figure(3).suptitle('Height vs Range Graph', fontsize=20)
plt.xlabel('Range (metres)', fontsize=16)
plt.ylabel('Height (metres)', fontsize=16)

plt.show() 
