mon_dict={'jan':31,'feb':28,'mar':31,'aprl':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
wk=[1,2,3,4,5,6,7]
def leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
           if (year % 400) == 0:
               return 1
           else:
               return 0
        else:
           return 1
    else:
    	return 0       

for i in range(1901,2001):
	for j in 