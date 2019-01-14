
# alternative class definition decorators

def classdef(initfunc):
    fname = initfunc.__name__
    classtype = type(fname, (object,), {})
    self_ = classtype()
    def wrap(*args, **kwargs):
        initfunc(self_, *args, **kwargs)
        return self_
    
    return wrap

def classfunc(classobj):
    def decor(func):
        fname = func.__name__
        setattr(classobj, fname, func)
    return decor

@property
def foo():
    pass


# use of decorators

@classdef
def MyClass(self, name, intval, listval):
    self.name = name
    self.intval = intval
    self.listval = listval

    @classfunc(self)
    def info():
        return 'MyCl info: %s, %d' % (self.name, self.intval)

tobj = MyClass('vasya', 123, 1.5)

print(tobj.name, ' ', type(tobj))
print(tobj.info())

