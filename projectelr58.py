import math
d=1
i=1
s=1
a=[]
p=0
def prime(n):
	for j in range(2,int(math.sqrt(n))+1):
		if n%j==0:
			return 0
	return 1		
while True:
	d+=4
	for j in range(4):
		s=s+2*i
		#print(s)
		if prime(s)==1:
			p+=1
			#a.append(s)
	'''if i==5:
		print(d,i,s)
		print(a)
		break'''		
	if (p/d)*100 < 10:
		print (i*2+1)
		print(d,i,s)
		print(a)
		break
	i+=1
			