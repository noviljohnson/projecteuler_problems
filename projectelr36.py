sum1=0
def pall(a):
	c=str(a)
	b=c[::-1]
	#print(b," ",c)
	if c==b:
		#print(b," ",c)
		return 1
	return 0	
def bin_pall(a):
	c=str(bin(a))
	b=c[:1:-1]
	if b==c[2:]:
		return 1
	return 0

for i in range(1,1000000):
	if pall(i)==1 and bin_pall(i):
		print(i)
		sum1+=i
print(sum1)		
#
