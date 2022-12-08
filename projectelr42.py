#path="C:\Users\AAA\Pictures\d_pics"
w_file=open("p042_words.txt",'r')
import string

#print(w_file.read(5))
l=list(w_file.read())

s_total=[]
alpha=list(string.ascii_uppercase)
tri_vals=[]
for i in range(20):
	tri_vals.append((i*(i+1))//2)
print(tri_vals)	
c=0	
sum1=0
for i in l:
	if i in alpha:
		sum1=sum1+ord(i)-64
	if i==",":
		s_total.append(sum1)
		sum1=0
for i in s_total:
	if i in tri_vals:
		c=c+1
print(c)				