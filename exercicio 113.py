string = ""
while True:
	a = [int(x) for x in input().split()]
	if a[0] > a[1]:
		string += "Decrescente\n"
	elif a[0] < a[1]:
		string += "Crescente\n"
	else:
		print(string, end="")
		break

