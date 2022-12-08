import random 
import itertools 
import math
l=[1,2,3,4,5,6,7,8]
def prime(a):
	for i in range(2,int(math.sqrt(a))+1):
		if a%i==0:
			return 0
	print(a)		
	return 1		
def check(s):	
	for i in s[::-1]:
		#print(i,type(i))
		if prime(int(i))==1:
			print(i)
			return 1
	return 0	
while True:
	l1=list(itertools.permutations(l))
	print(l)
	s=[]
	for i in l1:
		temp=""
		for j in i:
			temp=temp+str(j)
		s.append(temp)
	if check(s)==1 or len(l)<=4:
		break
	p=l.pop()			
#print(s[1],len(s))
