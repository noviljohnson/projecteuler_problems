pl=[1]
'''
for i in range(2,10001):
	n=(i*(3*i-1))//2
	pl.append(n)
print(len(pl))	
d=0	
for i in range(len(pl)):
	for j in range(i):
		if pl[i]-pl[j] in pl and pl[i]+pl[j] in pl:
			d=pl[i]-pl[j]
			print(d)
			break			
	if d>0:
		break		
'''
i=2
d=0
while True:
	n=(i*(3*i-1))//2
	pl.append(n)
	for j in pl:
		if n-j in pl:
			m=0
			k=i

			while m<=n+j:
				m=(k*(3*k-1))//2
				if m==n+j:
					print(n-j,n,j)
					d=n-j
					break
				k=k+1

	if d>0:
		break
	i=i+1
	
print(d)