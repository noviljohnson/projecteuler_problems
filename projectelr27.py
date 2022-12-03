import math
#import sympy
'''def prime(a):
	for i in range(2,int(math.sqrt(a)+1)):
		if a%i==0:
			return 0
	return 1
def num(n,a,b):
	i=int(n**2+a*n+b)
	return i
'''
def prime(a):
	if a==1 or a==0:
		return 0
	for i in range(2,int(math.sqrt(a))+1):
		if a%i==0:
			return 0
	return 1

max_num=0	

for a in range(-999,1000):

	for b in range(max(2,1-a),1000):
		n=0
		i=0
		while True and b>0:
			num=n**2+a*n+b
			if num>0 and prime(num)==1:
				i+=1 
			else:break	
			n+=1
		if max_num<i:
			max_num=i
			#print(max_num)
			ax=a
			bx=a
			pro=a*b

print(pro," ",ax," ",bx,max_num)
