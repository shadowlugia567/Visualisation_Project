import matplotlib.pyplot as plt 
import numpy as np 


G=6.673*(10**-11)

M = float(input('Enter the mass of the bigger body: '))
m = float(input('Enter the mass of the smaller body: '))
rp = float(input('Enter the periapsis in m: '))
vp = float(input('Enter the v in m/s: '))

""" #Data for testing. Using the Sun and the Earth.
m=5972000000000000000000000
M=1989000000000000000000000000000
rp=147100000000
vp=30290"""

E = (0.5*m*vp**2) - ((G*M*m)/rp)
L = m*rp*vp
mu = G*(m+M)
h = L/m
p = (h**2)/mu

e = (p/rp) - 1

print("The eccentricity is",e)
print("Semilatus rectum is",p)
print("The energy is",E)
print("The angular momentum is",m)

if(e > 1):
    print("The orbit's shape is hyperbolic")
    
if(e == 1):
    print("The orbit's shape is parabolic")
    
if(e > 0 and e < 1):
    print("The orbit's shape is elliptical")
    
if(e == 0 ):
    print("The orbit's shape is circular")
        
cos = np.cos
pi = np.pi


theta = np.linspace(0,2*pi, 360)
r = p/(1+e*cos(theta))
plt.polar(theta, r)

print(np.c_[r,theta])

plt.show()
