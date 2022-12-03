d=10
l=0
for i in range(1,1000):
	if i<10:
		d=10
	elif i<100:
		d=100
	elif i<1000:
		d=1000	
	if d%i is not 0:
		c=0
		fr=[0]
		q=[1]
		while True:
			if q[c]*10%i in q:
				break
			else:	
				q.append(q[c]*10%i)
				fr.append(q[c]*10//i)
			c+=1
		if l<len(fr):
			l=len(fr)
			din=i
print(din)			