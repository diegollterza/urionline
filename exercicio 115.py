res = ""
while True:
	point = [int(x) for x in input().split()]
	if point[0] == 0 or point[1] == 0:
		print(res,end="")
		break
	if point[0] > 0:
		if point[1] > 0:
			res += "primeiro\n"
		else:
			res += "quarto\n"
	else:
		if point[1] > 0:
			res += "segundo\n"
		else:
			res += "terceiro\n"
