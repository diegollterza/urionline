n = int(input())
vet = [input() for i in range(n)]
coelhos = 0
ratos = 0
sapos = 0
for i in range(n):
	par = vet[i].split()
	if par[1] == 'C':
		coelhos += int(par[0])
	elif par[1] == 'R':
		ratos += int(par[0])
	else:
		sapos += int(par[0])
total = ratos+coelhos+sapos
print('Total: %d cobaias' % (total))
print('Total de coelhos: %d' % (coelhos))
print('Total de ratos: %d' % (ratos))
print('Total de sapos: %d' % (sapos))
print('Percentual de coelhos: %.2f %%' % (coelhos*100/total))
print('Percentual de ratos: %.2f %%' % (ratos*100/total))
print('Percentual de sapos: %.2f %%' % (sapos*100/total))
