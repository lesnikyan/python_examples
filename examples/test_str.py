

from pprint import pr

pr.print_on = True

# printOn = True
# def pr(*args, **kwargs):
#     if printOn: print(*args, **kwargs)

pr('1: %d, 2: %d, 3: %s' % (111, 222, 'ccc'))

pr('name: %(name)s, age: %(age)d' % {'name':'Vasya', 'age': 25})

name = 'Osya'
pr(f'var name = {name}')




