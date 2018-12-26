import math

from pprint import pr

pr.print_on = False


pr ("hello!")
pr("циферки: {}, {}".format(11,22))
s = '''hello 2 
'''
pr(s)


for i in range(10, 20, 3) :
	if i%2 == 0 :
		pr ("even: {}".format(i))
	else: 
		pr ("odd:  {}".format(i))
		

words = ['aaa', 'bbb', 'ccc', 'ddd']
for w in words:
	pr (w)

for i in range(len(words)):
	pr ("{} : {}".format( i, words[i]))

for x in list(range(10)):
	if x % 2 == 0:
		pr("- {}".format(x))
	else:
		pass

def primes(max):
    nums = []
    for cur in range(2, max+1):
        maxArg = math.floor(math.sqrt(cur))
        if checkByPrev(cur, maxArg, nums):
            nums.append(cur)
    return nums

def checkByPrev(x, max, prev):
    for arg in prev:
        if arg > x:
            return True
        if x % arg == 0:
            return False
    return True

primeList = primes(20)
pr("primes: " + str(primeList))

def primeNear(max):
    #nums = []
    pr("cur: ")
    lastNum = 0
    for cur in range(2, max+1):
        if checkPrime(cur):
            lastNum = cur
            #pr("{}".format(cur), end = ("\n" if cur%20==0 else " "));
    pr("")
    return lastNum # nums[-1]

def checkPrime(num):
    #if num % 2 == 0:
        #return False
    maxArg = math.floor(math.sqrt(num)) + 1
    for i in range(2, maxArg, 1):
        if num % i == 0:
            return False
    return True

num = 1000000
pr("prime near {}: {}".format(num, primeNear(num)))

def multarg(*args, **args2):
    for v in args:
        pr (v, end=', ')
    pr("\n---")
    keys = sorted(args2.keys())
    for k in keys:
        pr("{} : {}".format(k, args2[k]))
    pr("---")

multarg(1,2,3, 'asd', 'zxc', nnnn=555, mmmm='qwerty');    

nums = [x for x in range(100) if checkPrime(x) and x > 50]
pr(str(nums))

pr([x + y + z for x in [3,5,7] for y in[20, 40, 60] for z in [100, 200, 300] if checkPrime(x + y + z) ])

nums = [0,1,2,3,4,5,6,7,8,9]
pr(nums[-4:-2])
nums[2:5] = [10,20,30]
nums[6:8] = []
pr(nums)
pr(*nums)

d = {'color' : 'red', 'size': 16, 'famely': 'Arial'}
for k, v in d.items():
    pr("{} : {}".format(k,v))

#names = {'aaa', 'bbb', 'ccc', 'ddd'}
#names.add('abc');
#pr(names)
#pr(sorted(names))

'''---  Lambdas  ---'''

def fltr(arrr, func):
    return [x for x in arrr if func(x)]

arr = range(10, 99)

def lim(minVal, maxVal):
    return lambda x: x > minVal and x < maxVal

#lim20_80 = lim(20, 80)
pr(fltr(arr, lambda x : lim(20, 80)(x) and checkPrime(x)))

# C:\Users\Sergio\Documents\python_examples\python_examples
