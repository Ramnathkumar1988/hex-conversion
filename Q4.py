def decompose(seta):
        DNA = ['A','T','C','G']
	 seta = seta.strip()
	dict = {}
	dict['Other'] = 0
	for i in range(0, len(seta)):
		if seta[i] not in DNA:
        		print 'WARNING: Found illegal character', seta[i], 'at position', i

	for char in seta:
		if char in dict: 
	   		dict[char] += 1
		elif char in DNA:
	   		dict[char] = 1
		else:
	   		dict['Other'] += 1
	print dict	    
decompose("CTATCGzGCACCCTTTCAG CA")

#PROGRAM EXPLANATION: Gave everything in a function called decompose and then called it. A empty dictionary called dict is declared and then others=0 is added to it. A list called DNA is also declared with stings A,T,C,G. Inside a for loop the range of letter entered (DNA Strand in this case) is run as index from 0 to lenth(seta)-1. and if the string for the particular index is not found in DNA then warning is typed. Then in another for loop Each character in seta is matchd for corresponding one is dict. If it is not there the character is added or else the value of that particular character key is incremeneted by 1. Then finally printed and function called in last line.
