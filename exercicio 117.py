i = 0
soma = 0
res = ""

while i != 2:
	a = float(input())
	if(a<0 or a > 10):
		res += "nota invalida\n"
	else:
		i += 1
		soma += a

print(res, end="")
print("media = %.2f" % (soma/2))