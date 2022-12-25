"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

Evaluate the sum of all the amicable numbers under 10000.
"""


from collections import defaultdict

def factors(i):
    l = [1]
    for j in range(2,int(i**(0.5))+1):
            if i%j == 0:
                l.append(j)
                l.append(i//j)
    return sum(l)

dict_facts_sums = defaultdict()
dict_facts_sums[1] = 0
amic_set = set()

sum_amic = 0
for i in range(1,10001):       

    if i not in dict_facts_sums.keys():
        sum_facts_a = factors(i)  # returns the sum of factors of i also equla to b
        dict_facts_sums[i] = sum_facts_a  # sum_facts_a is b

        # 
        if  sum_facts_a not in dict_facts_sums.keys():
            sum_facts_b = factors(sum_facts_a)    # sum_facts_b  is sum of factors of b which has to equal to a or i
            dict_facts_sums[sum_facts_a] = sum_facts_b 

        if i ==  dict_facts_sums[sum_facts_a] and i != sum_facts_a:  # d(a) = b and d(b) = a and a != b
            print(i,sum_facts_a)
            amic_set.add(i)
            amic_set.add(sum_facts_a)
            # sum_amic += sum([i,sum_facts_a])
print(sum(amic_set))