import math
c=0
s=set()

def pd(a,b,i):
	st=str(a)+str(b)+str(i)
	cm=set("123456789")
	if cm==set(st):
		return 1
	else:
		return 0	
for i in range(100,10000):
	for j in range(2,int(math.sqrt(i)+1)):
		if i%j==0:
			c=pd(j,i//j,i)
			if c==1:
				s.add(i)
				print(s)
				

print(sum(s))		
'''
import math


def compute():
	# For contradiction suppose a candidate (x, y, z) has z >= 10000.
	# Then x*y consumes at least 5 digits. With the 4 (or fewer) remaining digits, even the
	# upper bound of x=99 and y=99 produces a product of x*y < 10000, which is unequal to z.
	# Therefore we need the product z < 10000 to be able to find possible x and y values.
	ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
	return str(ans)


def has_pandigital_product(n):
	# Find and examine all factors of n
	for i in range(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False


if __name__ == "__main__":
	print(compute())
	'''	