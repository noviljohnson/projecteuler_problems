l="0"
i=1
while len(l)<=1000000:
	l=l+str(i)
	i=i+1
print(len(l),l[1])
p=1	
for i in range(7):
	print(l[10**i])
	p=p*int(l[10**i])
print(p)	