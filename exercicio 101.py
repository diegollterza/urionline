nums = []
while True:
	n = [int(x) for x in input().split()]
	if n[0] <= 0 or n[1] <= 0: break
	n.sort()
	nums.append(n)
	
for i in range(len(nums)):
	s = 0
	for j in range(nums[i][0], nums[i][1]+1):
		print(j, end=' ')
		s += j
	print("Sum=%d" % s)