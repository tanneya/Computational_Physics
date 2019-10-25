from numpy import *
from pylab import *
from numpy.fft import rfft2,irfft2

#load data
img=loadtxt('blur.txt')
#show the image
imshow(img,cmap='gray')
show()
#define the dimension of the image
N=img.shape[0]
M=img.shape[1]
sigma = 25

#calculate the density plot
density = zeros(img.shape)

#define the density function
def f(x,y):
    return e**(-(x**2+y**2)/(2.*sigma**2))

#make the left bottom corner of the plot
for i in range(int(N/2)):
    for j in range(int(M/2)):
        density[i,j]=f(i,j)
#define the rest of the plot
for i in range(int(N/2)+1):
    for j in range(int(M/2)+1):
        density[i,-j]=density[i,j]
        density[-i,j]=density[i,j]
        density[-i,-j]=density[i,j]
#shwo the density plot
imshow(density,cmap='gray')
show()
#calculate the Fourier Transform Coefficient for the devonvoluted image 
ck_image=rfft2(img)
ck_gaussian=rfft2(density)
ck_final=zeros(ck_image.shape,complex)
epsilon=10**-3  
for i in range(ck_image.shape[0]):
    for j in range(ck_image.shape[1]):
        if abs(ck_gaussian[i,j]) >= epsilon:
            ck_final[i,j]=ck_image[i,j]/ck_gaussian[i,j]
        else:
            ck_final[i,j]=ck_image[i,j]

#inverse transform 
imshow(real(irfft2(ck_final)),cmap='gray') 
show()