
from pprint import p
import time as tm

s = 'aaabbbsssdddeeefff'

s = s[::4]

p(s)

s = '-'.join([(c*3).capitalize() for c in s]) + ' '
s *= 3
p(s)

p(12)

p([1,2,3])

p({'aa', 'bb', 'cc'})

p({'a-key':'aaa', 'b-key':'bbb', 'c-key':1234567})

#p(tm.time())
#tm.sleep(1)
#p(tm.time())


#tm.start()
#p(tm.time())
t1 = tm.time()
#print('t1 ',t1)
s = ''
z = 'a'
count = 10 ** 6
for i in range(count):
    s += z
t2 = tm.time()
#print('t2 ',t2)
p('1 len(s) = %d' % len(s))
p("1 time1 = %f" % (t2 - t1))

t1 = tm.time()
s = ''
z = 'a'
s = ''.join([ 'a' for i in range(count)])
t2 = tm.time()
p('2 len(s) = %d' % len(s))
p("2 time1 = %f" % (t2 - t1))



