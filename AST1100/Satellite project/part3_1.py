from AST1100SolarSystem import AST1100SolarSystem
import numpy as np
from numpy import *
from PIL import Image

#Konstanter
theta0= pi/2
alpha=(70/180.)*pi

#Henter bildet jeg har tatt med satelitten
img=Image.open('Image0005.png')
#crop_rectangle=(0,0,900,900)
#cropped_img=img.crop(crop_rectangle)
#cropped_img.show()
pixels=np.array(img)
'''
#Teller antall piksler i x- og y-retning
width=len(pixels[0,:])
height=len(pixels[:,0])

#Henter inn himmelkula
sky=np.load('skymap.npy')
pxsky=np.array(sky)

#Gjor om disse til piksler i xy
extremal=2*sin(alpha/2)/(1+cos(alpha/2))
x_list=np.linspace(-extremal, extremal, width)
y_list=np.linspace(-extremal, extremal, height)

images=np.zeros(shape=[360,height,width,3],dtype=uint8)
for x in range(len(x_list)):
    for y in range(len(y_list)):
        rho=sqrt(x_list[x]**2+y_list[y]**2)
        c=2*arctan(rho/2.)
        a=arctan(x_list[x]*sin(c)/rho*sin(theta0)*cos(c)-y_list[y]*cos(theta0)*sin(c))
        theta=pi/2-arcsin(cos(c)*cos(theta0)+y_list[y]*sin(c)*sin(theta0)/rho)
        for phi0 in range(360):
            phi=phi0+a
            pix=AST1100SolarSystem.ang2pix(0,theta,phi)
            images[phi0,y,x]=pxsky[pix]

outfile=open('images.npy','wb')
np.save(outfile, [images])
'''
#Henter piksler himmelkule
infile=open('images.npy', 'rb')
[images]=np.load(infile)

#Bruker mkm til aa sammenligne disse
lms=np.zeros(360)
for degrees in range(360):
    D=(images[degrees]-pixels)**2
    lms[degrees]=sum(D)
print np.argmin(lms)
