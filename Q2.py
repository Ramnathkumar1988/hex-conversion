import sys
line = ''
todelu = []
todelx = []
indextogo = []
item = sys.stdin.read()
item = item.strip()
hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
for i in range(0, len(item)):
	if item[i] == '\\':   #\ is at 1
		if (item[i+1] == 'u') and item[i+2] in hex and item[i+3] in hex and item[i+4] in hex and item[i+5] in hex:  #u at 2		
			for l in range(i, i+6):
				todelu.append(l)
	
for i in range(0, len(item)):
	if item[i] == '\\': 
		if (item[i+1] == 'x') and item[i+2] in hex and item[i+3] in hex:	
			for k in range(i, i+4):
				todelx.append(k) 
indextogo=todelu+todelx                                            
for i in range(0, len(item)):
	if i not in indextogo:
		line = line + item[i]
print(line)
toremove = []
line = ''	
#PROGRAM EXPLANATION: the program looks for \and when it finds it enters in a if condition and looks for u followed by one of the letters in hex list. If it is there then the index of the letter is appended to todelu and todelx list respectively. Finally both the list are combined to indextogo list. Then a for loop is used to look for each item index number in the indextogo list, idex numbers which are not there are converted to respective string and then added to line

#1
#2\u5678
#1\x1234

#SETA
#as daf 
#h\u0024100,000
#dsd\xas10

#SETB
#as daf 
#h100,000
#dsd\xas10

#SETC
#as daf
#h


