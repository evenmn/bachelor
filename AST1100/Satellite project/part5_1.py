'''
Satellitten gar i sirkelbane rundt planet1. Den slipper ut en landingsenhet, 
som vil ha samme hastighet som satellitten nar den slippes ut. Landingsenheten 
gjor en boost i motsatt retning av bevegelsesretningen, slik at den far lavere 
hastighet og begynner a falle inn mot planeten. Den foretar en ny boost nar den
er i passe hoyde slik at den igjen gar i en stabil sirkelbane. Deretter tar jeg
bilder av overflaten (tenker egentlig a ta bilder med jevne mellomrom hele veien
'''
#Important imports
import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem
import pylab
seed=87
mSS=AST1100SolarSystem(seed)
N=mSS.numberOfPlanets

#Constants
RS1=94335119.6452           #Radius of satellite orbit
RP1=13339971.168            #Radius of planet1
MP1=3.91604892482e+25       #Mass of planet1
MS=11000                    #Mass of satellite
Ml=900                      #Mass of lander
mp=1.67e-27                 #Proton mass
Cd=1                        #Surface form lander
A0=2                        #Testing this area
A1=200
A2=100
rho0=2.28085544816          #Calculated density constant
mu=23.7559995364
kB=1.38e-23                 #Boltzmanns constant
T=230                       #Temperature surface planet 1, K
P=183190.2273               #Rotation period, s
g=14.78                     #Planet1 gravity on surface
G=6.67428e-11               #Gravitation constant
time=300000                 #Time
dt=10.                      #Timestep
N=int(time/dt)              #Number of timesteps
I=N                         #How many timestep that's plotted

#Arrays
sx=np.zeros([N+1,3])        #Satellite position array
sv=np.zeros([N+1,3])        #Satellite velocity array
t=np.zeros(N+1)             #Time array

#Initial condition
sx[0]=[35896801.77423237,  -4375956.13335888,0.0]
sv[0]=[-642.12543265,6000.0,0.0]
t[0]=0

#Gravitation function
def gravity(X,M):
    r=np.linalg.norm(X)
    F=-(G*M*MP1/r**3)*X
    return F

#Air force function
def friction(X,V,A):
    r=np.linalg.norm(X)             #Distance from planet center
    z=r-RP1
    rho=rho0*np.exp(-mu*mp*g*z/kB*T)
    VEL=[2*np.pi*r/P,0.0,0.0]
    F=-0.5*rho*Cd*A*(V-VEL)
    return F

#Loop                                   #Euler-Chromer loop
for i in xrange(N):
    r=np.linalg.norm(sx[i])             #Distance from planet center
    #z=r-RP1
    #if i == 11263:
    #    vel=sv[i]
    #    print vel
    #    sv[i]=[2000.0,-760.99853268,0.0]
    #    #print vel-sv[i]
    #Take pictures
    #tid=i*dt
    #if tid >= 100:
    #    if int(repr(i)[-1]) == 0 and int(repr(i)[-2]) == 0 and int(repr(i)[-3]) == 0:
    #        theta=np.arccos(z/r)
    #        phi=np.arctan(sx[i,1]/sx[i,0])
    #        text_file=open('SatellitePictures.txt','a')
    #        text_file.write('picture   %.f   %.2f   %.2f   %f   %f   %f\n' % (i*dt,theta,phi,sx[i,0]/r,sx[i,1]/r,sx[i,2]/r))
    #Boost force
    if (r-RP1) < 30:
        FB=[0.0,-30000,0.0]
    else:
        FB=0.0
    Fd=friction(sx[i],sv[i],A2)
    Fg=gravity(sx[i],MS)           
    a=(Fg+Fd+FB)/MS
    sv[i+1]=sv[i]+a*dt
    sx[i+1]=sx[i]+sv[i+1]*dt
    t[i+1]=t[i]+dt

#text_file=open('SatellitePictures.txt','a')
#text_file.write('boost   112628   -2000   -1000   0.0')

#Lander
start=1000#11263
M=np.linspace(start,N,N-start+1)
lx=np.zeros([len(M)+start+1,3])
lv=np.zeros([len(M)+start+1,3]) 
lx[start]=[35896801.77423237,  -4375956.13335888,0.0]
lv[start]=[-642.12543265,0.0,0.0]
for i in M:                   
    r=np.linalg.norm(lx[i])
    Fg=gravity(lx[i],Ml)
    if r > 13000:
        Fd=friction(lx[i],lv[i],A0)
    else:
        Fd=friction(lx[i],lv[i],A1)
    a=(Fg+Fd)/Ml
    lv[i+1]=lv[i]+a*dt
    lx[i+1]=lx[i]+lv[i+1]*dt
    if r < RP1:   #Break if lander hits planet
        I=i
        print i*dt
        print 'OH SHIT! YOU CRASHED THE LANDER!'
        break

#Plot
n=500                                   #Number of angles
number=2                                #Number of planet circles
theta0=np.linspace(0,2*np.pi,n)          #Angles
radi=np.linspace(0,RP1,number+1)
RP=np.zeros(shape=[number+1,n,2])
RS0=np.zeros([n,2]);RS=np.zeros([n,2])
RP0=np.zeros([n,2])
for i in range(n):
    t=theta0[i]
    for j in range(number+1):             #Making solid planetplot
        k=radi[j]
        RP[j][i]=[k*np.cos(t),k*np.sin(t)]
        plt.plot(RP[j][:,0],RP[j][:,1],'b')
        plt.hold('on')
    RS0[i]=[RS1*np.cos(t),RS1*np.sin(t)]
    RP0[i]=[RP1*np.cos(t),RP1*np.sin(t)]

#plt.plot(RS0[:,0],RS0[:,1],'-g')
plt.plot(sx[0,0],sx[0,1],'ok',label='start')
plt.plot(sx[:I,0],sx[:I,1],'r')
plt.plot(lx[start:I,0],lx[start:I,1],'g')
plt.plot(0.0,0.0,'w.')
plt.axis('equal')
plt.xlabel('x-retning')
plt.ylabel('y-retning')
#plt.legend(['a','b','c','d','e','f','g'])
plt.savefig('landing.png')
plt.show()
'''
#Animate
axis=(-1.0e8,1.0e8)
pylab.ion()
fig=plt.figure()
ax=fig.add_subplot(111,autoscale_on=False,xlim=axis,ylim=axis)
line1,=ax.plot(sx[0],'b-o')
line2,=ax.plot(lx[start],'r-o')
line3,=ax.plot(RP0[:,0],RP0[:,1],'r')
line4,=ax.plot(0.0,0.0,'k-o')
#plt.axis('equal')
while True:
    for i in xrange(N):
        k=i*dt*10
        line1.set_data(sx[k,0],sx[k,1])
        line2.set_data(lx[k,0],lx[k,1])
        pylab.draw()
'''
