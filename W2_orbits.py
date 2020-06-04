from vpython import*
from math import sqrt

scene = canvas()

M = float(input('Enter the mass of the bigger body: '))
m = float(input('Enter the mass of the smaller body: '))
F = float(input('Enter the Force in N: '))
A = float(input('Enter the centripetal acceleration in m/s^2: '))

s=sphere (pos=(vector(0,0,0)), radius=2, make_trail=True, retain=5000000)

o=sphere (pos=(vector(0,0,0)), radius=1, make_trail=True, retain=5000000)
o.velocity=vector(0,0,0)

G=6.673*(10**-11)

r = sqrt(((G*m*M)/F))
v = sqrt((r*A))

t=0
dt=0.0000001

while t<=10000000000000000:
    rate(100)
    
    
    o.pos.x = s.pos.x + r*cos(v*t)
    o.pos.y = s.pos.y + r*sin(v*t)
	
    t=t+dt	
print("End of program")