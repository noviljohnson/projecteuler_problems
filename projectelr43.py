#import itertools
from itertools import permutations
l=list(permutations([0,1,2,3,4,5,6,7,8,9]))

#print(l[1],l[3])
#s="asdfgh"
#l=list(permutations(s))
#print(len(l),l[0])
prime_list=[0,2,3,5,7,11,13,17]
total=0
num=[]
for i in l:
	c=0
	
	for j in range(1,len(i)-2):
		s_num=100*i[j]+10*i[j+1]+i[j+2]
		#print("s_num=",s_num)
		if s_num%prime_list[j]==0:
			c=c+1
			
		else:
			break
	if c==7:
		sum1=""
		for j in range(len(i)):
			sum1=sum1+str(i[j])
		#print(sum1)
		total=total+int(sum1)

print(total)
			