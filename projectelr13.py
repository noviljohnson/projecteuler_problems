fo=open("projectelr13.txt","r")
s=0
for i in range(100):
	s=s+int(fo.read(50))
	t=fo.read(1)
print(s)
st=str(s)
print(st[0:10])
