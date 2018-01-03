n = int(input())
nums = [[int(x) for x in input().split()] for i in range(n)]

def test_odd(n):
	return True if n % 2 != 0 else False

def sum_odds(a, b):
	s = 0
	if a > b:
		n = a
		a = b
		b = n
	for i in range(a+1,b):
		if test_odd(i):
			s += i
	return s

for i in range(n):
	print(sum_odds(nums[i][0],nums[i][1]))