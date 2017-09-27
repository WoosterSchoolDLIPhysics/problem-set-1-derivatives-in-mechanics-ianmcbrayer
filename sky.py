from pylab import *

t0 = 0.0 #initial time
tf = 50.0 #time fallen
dt = 1. #step size

t = arange(t0,tf,dt)
v = zeros(len(t))
v0 = 0
v[0] = v0

#define constants
b = .10 #drag coefficient
g = 10 #gravity!
m = 1. #kg

for i in arange(1,len(t)):
    dv = (-b/m*v[i-1]-g)*dt
    v[i] = v[i-1] + dv
 

figure(1)
clf()
plot(t,v,'bo',markersize=5)
vt = -m*g/b
plot(t,vt*(1-exp(-b*t/m)),'plum',lw=2)
text(20,-37,r'$v(t) = v_T(e^{-\frac{bt}{m}}-1)$',size = 20,color = 'magenta')
plot(t,0*t+vt,'k--') #this is ye olde horizontal asymptote
plot(t,-g*t,'c--')
ylim(-120,0)