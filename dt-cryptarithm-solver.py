# python3 dt-cryptarithm-solver.py
# pypy3 dt-cryptarithm-solver.py
import random
import time

def getNumber(i):
	x = []
	for w in letterinput[i]:
		x.append(str(letternumber[w]))
	return int(''.join(map(str, x)))

letterinput = ['G', 'CGCH', 'BAJJ', 'KCKC', 'F', 'KCJB', 'KCKD', 'ACAH', 'EGBK']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
numbers = list(range(10))
check = False
c = 0
uniqrandom = []
start = time.time()
while check is False:
	random.shuffle(numbers)
	letternumber = dict(zip(letters, numbers))
	#uniqrandom.append(''.join(map(str, numbers)))
	c += 1
	if int(getNumber(0))+int(getNumber(3)) == int(getNumber(6)):
		if int(getNumber(1))*int(getNumber(4)) == int(getNumber(7)):
			end = time.time()
			cps = float(c/(end - start))
			print("Calulations: {:,} @{:,}/second".format(c, int(cps)))
			if int(getNumber(2))-int(getNumber(5)) == int(getNumber(8)):
				print(" ")
				print(letterinput[0] + "     +  " + letterinput[3] + " = "  + letterinput[6])
				print(str(getNumber(0)) + "     +  " + str(getNumber(3)) + " = " + str(getNumber(6)))
				print(letterinput[1] + "  x     " + letterinput[4] + " = "  + letterinput[7])
				print(str(getNumber(1)) + "  x     " + str(getNumber(4)) + " = " + str(getNumber(7)))
				print(letterinput[2] + "  -  " + letterinput[5] + " = "  + letterinput[8])
				print(str(getNumber(2)) + "  -  " + str(getNumber(5)) + " = "  + str(getNumber(8)))
				print(" ")
				print("Calculations total : {:,}".format(int(c)))
				#print("Calculations uniq  : {:,}".format(int(len(set(uniqrandom)))))
				print("Calculations/second: {:,}".format(int(cps)))
				print("Total time in sec. : {0:.2f}".format(float(end - start)))
				print(" ")
				print(letternumber)
				print(" ")
				check = True
