n = int(input())
leitura = [input().split() for s in range(n)]
num = [[float(i[j]) for j in range(len(i))] for i in leitura]

media = [((num[i][0]*2 + num[i][1]*3 + num[i][2]*5)/10) for i in range(n)]
for i in range(n):
 	print("%.1f" % media[i])