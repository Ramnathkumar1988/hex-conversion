import sys
import matplotlib.pyplot as plt
seta = raw_input('Enter data:')
seta = seta.strip()
dict = {}
xaxis = []
y = []
for char in seta:
	if char in dict: 
	   dict[char] += 2
	else:
	   dict[char] = 1	    
for char, count in dict.iteritems():
	sys.stdout.write("%d\t%s\n" % (count, char))
xaxis=dict.keys()
y=dict.values()
print(xaxis, y)
plt.plot(xaxis, y)
plt.show()

#Get raw_input and store in SETA. In for loop Each character in seta is matchd for corresponding one is dict. If it is not there, the character is added or else the value of that particular character key is incremeneted by 1. Then finally printed. The keys and values of the dict are stored in two different list xaxis and y respectively. matplotlip is the used. 

