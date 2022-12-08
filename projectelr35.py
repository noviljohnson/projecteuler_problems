import math

def prime(a):
		for i in range(2,int(math.sqrt(a)+1)):
			if a%i==0:
				return 0	
		return 1		
#prime_list=[i for i in range(9,999999,2) if prime(i)]
#print(prime_list)
'''new_list=[]
for i in prime_list:
	s=str(i)
	c=0
	temp=[]
	for j in range(0,len(s)):
		ns=int(s[j:]+s[:j])		
		if prime(ns):
		    #temp.append(ns)
		    c=c+1	
		else:
			break
	if c==len(s):
		#new_list.extend(temp)
		new_list.append(i)

print(len(set(new_list)))		#add 2357=4 externally 
'''		
'''	even=set("24680")
	s=str(a)
	if not even.intersection(set(s)):
import eulerlib, sys
if sys.version_info.major == 2:
	range = xrange


def compute():
	isprime = eulerlib.list_primality(999999)
	def is_circular_prime(n):
		s = str(n)
		return all(isprime[int(s[i : ] + s[ : i])] for i in range(len(s)))
	
	ans = sum(1
		for i in range(len(isprime))
		if is_circular_prime(i))
	return str(ans)


if __name__ == "__main__":
	print(compute())
'''

def clr_prime(i):
	s=str(i)
	c=0
	for j in range(len(s)):
		if prime(int(s[j:]+s[:j])):
			c=c+1
		else:
			return 
	if c==len(s):
		return i
prime_list=[i for i in range(9,999999,2) if clr_prime(i)]					
print(prime_list,len(prime_list))