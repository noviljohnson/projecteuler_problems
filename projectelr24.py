import itertools
l=set(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
#print(l[1000000])
#(2, 7, 8, 3, 9, 1, 5, 6, 0, 4)
l1=list(l)
l1.sort()
l2=l1[1000000-1]
print(l1[1000000-1])
num=0
for i in range(len(l2)):
	num=num+l2[i]*pow(10,len(l2)-i-1)
print(num)
print(len(l))

