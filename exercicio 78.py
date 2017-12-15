num = 100
pos = 0
biggest = -1
n = [int(input()) for i in range(num)]
for i in range(num):
	if(n[i]> biggest):
		biggest = n[i]
		pos = i+1
print(biggest)
print(pos)