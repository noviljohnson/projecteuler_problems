import collections
l=[]
for a in range(500):
	for b in range(a):
		for c in range(b):
			if a+b+c<=1000 and a*a==b*b+c*c:
				l.append(a+b+c)

count=collections.Counter(l)
print(count.most_common(1))