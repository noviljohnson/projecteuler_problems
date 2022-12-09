sum1=0
for i in range(1,1001):
	sum1=sum1+i**i
	#print(i**i," ",i)
l=str(sum1)
#print(sum1)
print(l[len(l)-10:])
#9110846700