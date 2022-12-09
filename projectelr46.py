import math
def prime(p):
	if p==1 or p==0:
		return 0
	for i in range(2,int(math.sqrt(p))+1):
		if p%i==0:
			return 0
	return 1			
n=33
c=0#checks for the requirments 
while True:
	y=1
	p=n-2*y*y
	if prime(n)==0: #n is required composite num 
		while p>0:
			if prime(p)==1:#p must be prime atleast once
				c=0        #for range of y
				break
			elif prime(p)==0:# other wise our requirement is satisfied			
				c=1
			y=y+1
			p=n-2*y*y
		if c==1:
			print(n)
			break		
	n=n+2	
'''
odd_num=prime+2*y*y
y be any int
we do this as
odd_num-2y*y=prime
'''