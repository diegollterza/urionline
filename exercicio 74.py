n = int(input())
aux = []
def odd(n):
	return False if n % 2 == 0 else True

def negative(n):
	return True if n < 0 else False

def result(n):
	if n == 0:
		print("NULL")
	else:
		result = "ODD " if odd(n) else "EVEN "
		result += "NEGATIVE" if negative(n) else "POSITIVE"
		print(result)


for i in range(n):
	aux.append(int(input()))
for i in range(n):
	result(aux[i])