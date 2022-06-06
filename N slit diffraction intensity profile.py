#This code is created by Souvik on 06/06/22
#Dedicated to Palash Nath Sir

#Importing libraries

import numpy as np
import matplotlib.pyplot as plt

#Constants:
#Opaque width
a = 1
#Ratio of Openning and Opaque width
r = 5
#Opening width
b = r*a
#Make sin(x) as x for small angle approximation

x = np.arange(-5,5,0.001)
#Alpha and Beta as p and t
p = np.pi*a*x
t = np.pi*(a+b)*x
#N denotes for no of slits
for N in range(1,7):
	
	#Equation to plot:
	y = (np.sin(p)/p)**2*(np.sin(N*t)/np.sin(t))**2

	#Plotting
	plt.subplot(3,2,N)
	plt.plot(x,y,'blue')
plt.show()
