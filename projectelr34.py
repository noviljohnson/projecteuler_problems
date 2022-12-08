fact_dict={'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880,'0':1}
fact_sum=0
sum_num=0
for i in range(3,1000000):#guess 1000000
	s=str(i)
	fact_sum=0
	for j in s:
		fact_sum=fact_sum+fact_dict[j]
	if i==fact_sum:
		print(i)
		sum_num=sum_num+i	

print(sum_num)
