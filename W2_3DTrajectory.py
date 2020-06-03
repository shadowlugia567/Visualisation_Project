from vpython import*

scene = canvas()
s=sphere (pos=(vector(0,0,0)), radius=0.25, make_trail=True, retain=5000000)
s.velocity=vector(0,0,0)
u = float(input('Enter the initial velocity in m/s: '))
A = float(input('Enter the angle(in radians(between 0 and pi/2): '))


time=(2*u*sin(A))/9.8 
t=0
dt=0.0001
s.velocity.x = u*cos(A)
s.velocity.y = u*sin(A)
while(t<=time):
    rate(10000)
    
    s.pos.x = s.pos.x+s.velocity.x*dt
    s.velocity.y =s.velocity.y+(-9.8)*dt
    s.pos.y = s.pos.y+ s.velocity.y*dt
    
    t=t+dt
