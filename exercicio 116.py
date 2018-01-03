n = int(input())
res = ""

for _ in range(n):
	div = [int(x) for x in input().split()]
	if div[1] == 0:
		res += "divisao impossivel\n"
	else:
		res += str(format(div[0]/div[1], '.1f')) + "\n"

print(res, end='')
