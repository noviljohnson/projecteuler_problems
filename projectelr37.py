import math
def prime(a):
	if a==1 or a==0:
		return 0
	for i in range(2,int(math.sqrt(a))+1):
		if a%i==0:
			return 0
	return 1

def l_prime(a):
	s=str(a)
	c=0
	for i in range(len(s)):
		#print("l",s[i:])
		if prime(int(s[i-1:])):
			c+=1
	if c==len(s): 
		return 1
	else:
		return 0

def r_prime(a):
	s=str(a)
	c=0

	for i in range(len(s)):
		#print("r",s[:len(s)-i])
		if prime(int(s[:len(s)-i])):
			c+=1
	if c==len(s): 
		return 1
	else:
		return 0
sum1=0
a=11
c=0
while(True):
	if prime(a):
		#print(a)
		if l_prime(a) and r_prime(a):
			print("lr ",a)
			sum1+=a
			c+=1
	if c==11:
		break	
	a=a+1		
print(sum1)