import math

def delno(n):
	r = 1
	for i in range(int(math.sqrt(n)), 1, -1):
		c = i**2
		if (n % c == 0):
			return i

	return 1


n = int(input())

for i in range(n):
	inp = input()
	pos = inp.find("s")

	if (pos == 0):
		a = 1
		b = int(inp[5:-1])
	elif(pos != -1):
		a,b = inp.split("*sqrt(")
		a = int(a)
		b = int(b[:-1])
	else:
		a = int(inp)
		b = 1


	#print(str(a) + " " + str(b))
	#print("$$$$$$$$$$$")

	c = delno(b)
	a *= c
	b //= (c**2)

	if (a == 1):
		if (b == 1):
			print(str(b))
		else:
			print("sqrt({0})".format(b))
	elif(b == 1):
		print(str(a))
	else:
		print("{0}*sqrt({1})".format(a, b))

	#print(str(a) + " " + str(b))

