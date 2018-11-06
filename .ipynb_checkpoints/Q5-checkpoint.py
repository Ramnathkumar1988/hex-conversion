import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
def fact(n):
	if n > 1:
		return(n * fact(n-1))
	else:
		return(1)
def minus(m):
	m = m-1
	return(m)
#used this to perform (n-1) factorial
def beta(x,a,b):
	p = fact(minus(a+b))	
	q = fact(minus(a))
	r = fact(minus(b))
	t = x**(a-1)
	y = (1-x)**(b-1)
	beta = (p*t*y)/(q*r)
	return(beta)

a=float(input("Enter the value of a"))
b=float(input("Enter the value of b"))

print ("Type 1 to input x value manually")
print ("Type 2 to input x as a many valued vector implemented as python array")
choice=float(input("Enter choice 1 or 2"))

if choice == 1:
	x = float(input("Enter value of x"))
else:
	x = np.arange(.001,.999,.01008)
l = beta(x,a,b)
print(x)
print(l)
plt.plot(x,l)
plt.show()
#PROGRAM EXPLANATION: Factorial function is declared forllowed by minus functions for feeding n-1 to factorial. Beta definetion is given. Input for a and b is obtained from user and program throws two choices for x. 1. give one value or take it from a array vector (np.arange). beta is called and x and l are the x and y axis for matplot.  
