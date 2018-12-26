
from pprint import p
import functools as f

p(f.reduce(lambda x, y: x + y,  range(1, 101)))

p(3 and 5 and 7)

class FuncList:
    
    def __init__(self, foo):
        self.foo = foo
        self.arg = 1
    
    def set(self, arg):
        self.arg = arg
    
    def __call__(self, items):
        return [self.foo(item, self.arg) for item in items]

nums = list(range(1, 10))
p(nums)

foo_exp2 = FuncList(lambda x, y: x ** y)

foo_exp2.set(2)
p(foo_exp2(nums))

foo_exp2.set(3)
p(foo_exp2(nums))

foo_exp2.foo = lambda x, y: x * y * 10
foo_exp2.set(5)
p(foo_exp2(nums))

def foo1(foo):
    return lambda x: "[{}]".format(foo(x))

def foo2(foo):
    return lambda x: "<{}>".format(foo(x))

@foo1
@foo2
def foo3(x):
    return "{0} {0} {0}".format(x)

p(foo3('abc'))
    
