

def p(x):
    #if not (type(x) in [str, int, float]):
    if not isinstance(x, (str, int, float)):
        if isinstance(x, (list, set, dict)):
            x = str(x)
        elif isinstance(x, object):
            if not '__str__' in  x.__class__.__dict__.keys():
                x = objInfo(x)
            x = str(x)
        else:
            x = '?'+str(x)
        x = '>> ' + x
    print(x)


def objInfo(obj):
    return 'class ' + type(obj).__name__ + ' ' + \
        str(dict([(k, getattr(obj, k)) for k in obj.__class__.__dict__.keys() if not k.startswith('__')] )) # '''if not k.startswith('_')'''
    #objType = type(obj).__name__
    #vals = {}
    #for key in [k for k in obj.__class__.__dict__.keys() if not k.startswith('_')]:
        #vals[key] = getattr(obj, key)
    

class PrintWrapper:
    print_on = False

    def __init__(self, turn_on=False):
        self.print_on = turn_on

    def __call__(self, *args, **kwargs):
        if self.print_on: print(*args, **kwargs)

# printOn = False
# def pr(*args, **kwargs):
#     if printOn: print(*args, **kwargs)

pr = PrintWrapper(False)
