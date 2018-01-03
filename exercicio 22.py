def __parser(s):
	n1 = int(s[0:1])
	d1 = int(s[4:5])
	n2 = int(s[8:9])
	d2 = int(s[12])
	c = s[6]
	return n1,d1,n2,d2,c

def __sum(n1,d1,n2,d2):
	n = n1*d2 + n2*d1
	d = d1*d2
	return n, d

def __sub(n1,d1,n2,d2):
	n = n1*d2 - n2*d1
	d = d1*d2
	return n, d

def __multi(n1,d1,n2,d2):
	n = n1*n2
	d = d1*d2
	return n, d

def __div(n1,d1,n2,d2):
	n = n1*d2
	d = n2*d1
	return n, d

def __simplify(n,d):
	h = abs(n)
	for i in range(2,h+1):
		while(n%i == 0 and d%i == 0):
			n = n/i
			d = d/i

	return n, d

x = int(input())
string = ''

for i in range(x):
	s = input()
	n1, d1, n2, d2, c = __parser(s)
	if c == '+':
		n, d = __sum(n1,d1,n2,d2)
	elif c == '-':
		n, d = __sub(n1,d1,n2,d2)
	elif c == '/':
		n, d = __div(n1,d1,n2,d2)
	else:
		n, d = __multi(n1,d1,n2,d2)
	n2,d2 = __simplify(n,d)
	string += str(n) + "/" + str(d) + " = " + str(int(n2)) + "/" + str(int(d2)) + "\n" 
print(string)
