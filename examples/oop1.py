
 
'''oop examples'''

from pprint import p
 
#class Unit:
    #pass
    
class A:
    x = 2
    s = 'asdf'
    
    def __str__(self):
        return 'class ' + type(self).__name__ + str({'x': self.x, 's': self.s})
    
class B:
    a = 1
    b = 'abcde'
    c = [1,2,3]
    
class C(A):
    zz = 'In class C zz val'
    ss = 'no val'
    def __init__(self, ss):
        self.ss = ss
p(A())
#print(type(B()))
p(B())
c = C('new ss val')
p(c)
    
class Af:
    def foo(self, x):
        p('foo A: ' + x)
        
class Bf(Af):
    def foo(self, x):
        p('foo B: ' + x)
        
class BBf(Bf):
    def foo(self, x):
        p('foo BB: ' + x)
    
class Cf(Bf):
    def foo(self, x):
        p('foo C: ' + x)
        super(Cf, self).foo(x)
        super(Bf, self).foo(x)
        #super(BBf, self).foo(x) # Bad call: TypeError: super(type, obj): obj must be an instance or subtype of type

c = Cf()
c.foo('abc')
    
def partgen(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i: i+n]

class Matrix:
    _vals = []
    _w = 0
    _h = 0
    
    def __init__(self, w, h):
        self._vals = [0] * (w * h)
        self._w = w 
        self._h = h
        
    def get(self, x, y):
        index = self._prepareIndex(x, y)
        return self._vals[index]
    
    def set(self, x, y, val):
        index = self._prepareIndex(x, y)
        self._vals[index] = val
        
    def _prepareIndex(self, x, y):
        assert (x < self._w), 'Incorrect value of x param'
        assert (y < self._h), 'Incorrect value of y param'
        index = self._w * y + x
        assert (index < len(self._vals)), 'Incorrect selection index'
        return index
        
    def parts(self):
        return partgen(self._vals, self._w)

    def __str__(self):
        return "class Matrix:\n" +  "\n".join(["\t"+str(r) for r in self.parts()])
    
    def vals(self):
        return self._vals

x, y = 2, 3
m = Matrix(x, y)
for i in range(y):
    for j in range(x):
        m.set(j, i, 100+100*i+j)
p(m)
p(m.vals())
p(m.get(1,2))
#p(m.get(2,1))
#p(m.get(1,3))
class AAA:
    pass
p(AAA())

class Person:
    '''Person info '''

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    @classmethod
    def create(cls, *args):
        return cls(*args)

'''End of class '''

class Worker(Person):
    '''Worker as subclass of Person '''

    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, val):
        self.__salary = val

vasya = Person('Vasya', 21)
olya = Worker('Olya', 31, 1000)

vasya.age = 22
# olya.name = 'NoOlya' # AttributeError: can't set attribute
olya.salary = 1500.5

pedro = Person.create('Pedro', 41)
rembo = Worker.create('Rembo', 51, 2000)

rembo.salary = 3000

p('{}, {} yo'.format(vasya.name, vasya.age))
p('{}, {} yo, {} ue'.format(olya.name, olya.age, olya.salary))
p('{}, {} yo'.format(pedro.name, pedro.age))
p('{}, {} yo, {} ue'.format(rembo.name, rembo.age, rembo.salary))
