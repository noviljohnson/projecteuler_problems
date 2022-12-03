#pe18

#fo=open("projecteuler18.txt","r")
#to=open("projecteuler18.txt","r")

#pe67
fo=open("p067_triangle.txt","r")
to=open("p067_triangle.txt","r")


l=fo.readlines()
print(len(l))
'''tri=[]
for i in range(len(l)):
	print(l[i],type(l[i]))
	li=l[i]
	for j in range(0,i+1):
		#print(l[i])
		s=li[j:j+2]
		print(s)
		j=j+3
	#tri.append(int(s))
print(tri)	
'''
total=[]
for i in range(len(l)):
	tri=[]
	for j in range(i+1):
		s=to.read(2)
		sp=to.read(1)
		#print(s)
		tri.append(int(s))
	#print(tri)	
	total.append(tri)
for i in range(len(l)-2,-1,-1):
	for j in range(i+1):
		mx=max(total[i][j]+total[i+1][j],total[i][j]+total[i+1][j+1])
		total[i][j]=mx
print(total[0])
fo.close()
to.close()
