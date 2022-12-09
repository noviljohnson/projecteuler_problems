import math
def prime(a):
	for i in range(2,int(math.sqrt(a))+1):
		if a%i==0:
			return 0
	return 1
#def check(a):
#	s=str(a);
prime_l=[]
for i in range(1000,9999):
	if prime(i)==1:
		prime_l.append(i)
print(len(prime_l))


for i in range(len(prime_l)):
	s=set(str(prime_l[i]))
	for j in range(i+1,len(prime_l)):
		t=set(str(prime_l[j]))
		if t==s:
			d=prime_l[j]-prime_l[i]
			if set(str(d+prime_l[j]))==s and d+prime_l[j] in prime_l:
				print(prime_l[i],prime_l[j],prime_l[j]+d)
'''
for i in range(len(prime_l)):
	for j in range(i,len(prime_l)):
		d=prime_l[j]-prime_l[i]
		n=prime_l[j]+d	
		if n in prime_l:
			print(i)
			exit()				
'''
	