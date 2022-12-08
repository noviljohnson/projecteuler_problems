tri=[]
pen=[]
hexa=[]
'''
for i in range(144,10000):
	hexa.append(2*i*i-i)
for k in range(285,10000):
	tri.append((k*(k+1))//2)
for m in range(165,10000):
	pen.append((m*(3*m-1))//2)	
print(len(tri),len(pen),len(hexa),hexa[0],)
for i in range(10000,len(hexa)):
	if hexa[i] in tri:
		print(hexa[i])
'''		

'''
while True:
	h=2*n*n-n
	print("h=",h)
	m=n
	while True:
		p=(m*(3*m-1))//2
		print("p=",p)
		if m>h:
			break
		k=m
		while True:
			t=(k*(k+1))//2
			print(t)
			if t>p:
				break
			elif t==p and t==h:
				print(t)
				exit()
			k=k+1
	
		m=m+1
	n=n+1	
'''					

t=258
p=166
h=144

while True:
	T=(t*(t+1))//2
	while True:
		P=(p*(3*p-1))//2
		if P==T:
			print("p=",P)
			while True:
				H=h*(2*h-1)
				if H==P:
					print("H= ",H)
					exit()
				elif P<H:
					h=h-1
					break
				h=h+1
		elif T<P:
			p=p-1
			break 
		p=p+1
	t=t+1	
 
'''
we have to start from t=286,p=166,h=144
for a num T(from 268) series it enough to check up to T<P
same for P and H
'''