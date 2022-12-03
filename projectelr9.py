'''for c in range(1,1000):
	for b in range(1,c-1):
		for a in range(1,b-1):
			if a<b<c and a+b+c==1000:
				if a*a+b*b==c*c:
					print(a*b*c)
					exit()

'''
for a in range(1,1000):
	for b in range(a+1,1000):
		c=1000-a-b
		if a*a+b*b==c*c:
			print(a*b*c)
