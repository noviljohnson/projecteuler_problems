g=open("projectelr11.txt","r")
l=[]
for i in range(20):
	t=[]
	for j in range(20):
		t.append(int(g.read(2)))
		s=g.read(1)
	l.append(t)
	
print(len(l))	
mp=0
for i in range(17):
	k=3
	for j in range(17):
		p1=l[i][j]*l[i][j+1]*l[i][j+2]*l[i][j+3]
		p2=l[i][j]*l[i+1][j]*l[i+2][j]*l[i+3][j]
		p3=l[i][j]*l[i+1][j+1]*l[i+2][j+2]*l[i+3][j+3]
		p4=l[i][j+3]*l[i+1][j+2]*l[i+2][j+1]*l[i+3][j]
		mp=max(p1,p4,p2,p3,mp)
print(mp)