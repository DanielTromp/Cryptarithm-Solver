import random
import time
import numpy as np

#GCAG-GEH=GFKA
#DCC-GKD=HCJ
#JDAK-JAB=JECD
#GCAG+DCC=JDAK
#GEH+GKD=JAB
#GFKA+HCJ=JECD

reeks1 = "G"
reeks2 = "CGCH"
reeks3 = "BAJJ"
reeks4 = "KCKC"
reeks5 = "F"
reeks6 = "KCJB"
reeks7 = "KCKD"
reeks8 = "ACAH"
reeks9 = "EGBK"

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
#letters = list(set(reeks1+reeks2+reeks3+reeks4+reeks5+reeks6+reeks7+reeks8+reeks9))
#letters.sort()
print(letters)

check = False
count = 0
start = time.time()
while check is False:
	count += 1
	cijfers = np.arange(10)
	np.random.shuffle(cijfers)
	#print(cijfers)
	r1 = []
	for w in reeks1:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r1.append(c)
	r1 = ''.join(map(str, r1))
	#print(r1)

	r2 = []
	for w in reeks2:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r2.append(c)
	r2 = ''.join(map(str, r2))
	#print(r2)

	r3 = []
	for w in reeks3:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r3.append(c)
	r3 = ''.join(map(str, r3))
	#print(r3)

	r4 = []
	for w in reeks4:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r4.append(c)
	r4 = ''.join(map(str, r4))
	#print(r1)

	r5 = []
	for w in reeks5:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r5.append(c)
	r5 = ''.join(map(str, r5))
	#print(r5)

	r6 = []
	for w in reeks6:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r6.append(c)
	r6 = ''.join(map(str, r6))
	#print(r6)

	r7 = []
	for w in reeks7:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r7.append(c)
	r7 = ''.join(map(str, r7))
	#print(r1)

	r8 = []
	for w in reeks8:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r8.append(c)
	r8 = ''.join(map(str, r8))
	#print(r8)

	r9 = []
	for w in reeks9:
		for (l, c) in zip(letters, cijfers):
			if w == l:
				r9.append(c)
	r9 = ''.join(map(str, r9))
	#print(r9)
	#print(reeks1 + "  +  " + reeks4  + " = "  + reeks7)
	#print(r1     + "  +  " + r4      + " = "  + r7)
	if (int(r1)+int(r4)) == int(r7):
		#print(reeks1 + "  +  " + reeks4  + " = "  + reeks7)
		#print(r1     + "  +  " + r4      + " = "  + r7)
		if (int(r2)*int(r5)) == int(r8):
			print(reeks1 + "  +  " + reeks4  + " = "  + reeks7)
			print(r1     + "  +  " + r4      + " = "  + r7)
			print(reeks2 + "  x  " + reeks5  + " = "  + reeks8)
			print(r2     + "  x  " + r5      + " = "  + r8)
			print(" ")
			print(count)
			end = time.time()
			cps = float(count/(end - start))
			print("{0:.2f} calulations per second".format(cps))
			print(" ")
			if (int(r3)-int(r6)) == int(r9):
				print(reeks1 + "  +  " + reeks4  + " = "  + reeks7)
				print(r1     + "  +  " + r4      + " = "  + r7)
				print(reeks2 + "  x  " + reeks5  + " = "  + reeks8)
				print(r2     + "  x  " + r5      + " = "  + r8)
				print(reeks3 + "  -  " + reeks6  + " = "  + reeks9)
				print(r3     + "  -  " + r6      + " = "  + r9)
				print(" ")
				print(count)
				print(letters)
				print(cijfers)
				check = True


"""
print(reeks1 + " -  "  + reeks2 + " = "  + reeks3)
print(r1     + " -  "  + r2     + " = "  + r3)
print(reeks4 + "  -  " + reeks5 + " =  " + reeks6)
print(r4     + "  -  " + r5     + " =  " + r6)
print(reeks7 + "  -  " + reeks8 + " = "  + reeks9)
print(r7     + "  -  " + r8     + " = "  + r9)
"""
