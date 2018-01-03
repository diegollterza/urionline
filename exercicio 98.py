i = 0.0
j = 1.0
test = 5

while i<=2.1:
 	for x in range(3):
 		if (test%5!=0): 
 			print("I=%.1f J=%.1f" %(i,j))
 		else:
 			print("I=%d J=%d" %(i,j))
 		j += 1
 	j -= 2.8
 	i += 0.2001
 	test += 1

