def media():

	i = 0
	soma = 0
	res = ""
	b = 0

	while i != 2:
		a = float(input())
		if(a<0 or a > 10):
			print("nota invalida")
		else:
			i += 1
			soma += a

	print("media = %.2f" % (soma/2))

	while(b < 1 or b > 2):
		print("novo calculo (1-sim 2-nao)")
		b = int(input())

	if b == 1: media()

#main
media()