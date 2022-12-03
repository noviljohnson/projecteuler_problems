def gcd(a,b):
	t=a
	for i in range(1,t):
		if a%i==0:
			f=a/i
			if b%f==0:
				print(f)
				return f
			t=int(t/i)
	return 1			
sub_fraction=1
denominator=1
pro=1
for i in range(10,100):
	for j in range(10,100):
		fraction=i/j
		if fraction<1:
			s1=str(i)
			s2=str(j)
			if s1[1]==s2[0] and int(s2[1])!=0:
				sub_fraction=int(s1[0])/int(s2[1])
				if sub_fraction==fraction:
					divisor=gcd(i,j)
					pro=pro*i
					denominator=denominator*j
					print("ans=",denominator/pro)
#print(denominator)

