
from pprint import p 

gen_compr = (2 * x for x in range(20) if x % 3 == 0)
for n in gen_compr:
    print(n, end=', ')
print()

def num_gen(n, k):
    return (x for x in range(1, n) if x % k == 0)

for x in num_gen(50, 5):
    print(x*10, end=' ')
print()

# ***

dct = {'a' : 1,'b' : 2,'c' : 3}
dct2 = { k : [10 ** x * 10 + val for x in range(3)] for k, val in dct.items()}
p(dct2)

seq = {1,2,3,4,5}
seq2 = {x * 10 for x in seq}
p(seq2)

