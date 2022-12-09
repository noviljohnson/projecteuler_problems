import math 
def prime(a):
	for i in range(2,int(math.sqrt(a))+1):
		if a%i==0:
			return 0
	return 1
sum1=2
c=0
pl=[2]
l=0
t=0
for i in range(3,400000,2):
	if prime(i)==1:
		pl.append(i)
		sum1=sum1+i
		if sum1>1000000:
			while True:
				sum1=sum1-pl[c]
				if sum1<1000000:
					break
				c=c+1		
		if prime(sum1)==1:
			if sum1>l:
				l=sum1
				bp=sum1
			else:
				break	
print(bp)

						

