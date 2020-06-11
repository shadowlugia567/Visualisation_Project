from vpython import*
from math import sqrt

scene = canvas()

M = float(input('Enter the mass of the bigger body: '))
m = float(input('Enter the mass of the smaller body: '))
F = float(input('Enter the radius in m: '))
A = float(input('Enter the v in m/s: '))

s=sphere (pos=(vector(0,0,0)), radius=2, make_trail=True, retain=5000000)

o=sphere (pos=(vector(0,0,0)), radius=1, make_trail=True, retain=5000000)
o.velocity=vector(0,0,0)

G=6.673*(10**-11)

F = (G*m*M)/(r**2)
A = (v**2/r)

print(" The gravitational force between the two objects is: ",F," N")
print(" The Centripetal acceleration of the smaller object is: ",A, "m/s^2")


t=0
dt=0.0000001

while t<=10000000000000000:
    rate(100)
    
    
    o.pos.x = s.pos.x + r*cos(v*t)
    o.pos.y = s.pos.y + r*sin(v*t)
	
    t=t+dt	
print("End of program")
