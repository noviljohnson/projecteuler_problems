maxp=0
for i in range(999,500,-1):
	for j in range(999,500,-1):
		p=i*j
		s=str(p)
		st=set(s)
		if len(st)==3:
			if s[0]==s[5] and s[1]==s[4] and s[2]==s[3]:
				#print(i,j)
				if maxp<p:
					maxp=p
					print(maxp)
					
				
