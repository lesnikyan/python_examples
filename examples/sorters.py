import random
from pprint import p

src = [
    {'zaz':'1'}, {'wq':'7'},
    {'zax':'2'}, {'we':'8'},
    {'abc':'3'}, {'er':'9'},
    {'bbb':'4'}, {'rt':'10'},
    {'def':'5'}, {'ty':'11'},
    {'mkp':'6'}, {'yu':'12'}
]

sortedList = sorted(src, key = lambda x : list(x.keys())[0])

# for t in sortedList:
#     print(str(t))

src2 = [
    [3,3],[20,3],[10,2],[4,3],[100,4],[1,5]
]
src2.sort(key = lambda x: x[0])
print(str(src2))

random.seed(1001)
lst = []
minVal = 0
for i in range(10):
    t = []
    for sz in range(0, random.randint(3, 10)):
        t.append(random.randint(minVal, 9))
    lst.append(t)

def printLL(data):
    for t in data:
        print(str(t))

printLL(lst)
print()
lst.sort(key = lambda x : len(x))
printLL(lst)
print()
lst.append([])
random.shuffle(lst)
lst.sort(key = lambda x : x [0] if len(x) > 0 else minVal - 1)
printLL(lst)

class Item:
    def __init__(self, size, age):
        self.size = size
        self.age = age

    def __str__(self):
        return 'Item(size: {}, age: {})'.format(self.size, self.age) 

lst = [Item(10, 20), Item(20, 20), Item(20, 10), Item(10, 40), Item(10, 30)]

lst.sort(key = lambda item : (item.size, item.age))

print(str([str(x) for x in lst])) 
