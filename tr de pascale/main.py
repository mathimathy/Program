import numpy as np
m = int(input('m: '))
a = np.zeros((m,m))
a[0,0] = 1
b = 1
l=1
c=1
while b <= m-1:
	a[b, 0] = 1
	b+=1
while l <= m-1 and c <= m-1:
	a[l,c] = a[l-1,c] + a[l-1, c-1]
	if l == m-1:
		l = 1
		c+=1
	else:
		l+=1

print(a)
with open('tr.txt', 'w+') as fic:
	fic.write(str(a))