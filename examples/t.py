
printOn = False

def pr(*args, **kwargs):
    if printOn: print(*args, **kwargs)

pr('|' + 'qwerty'.center(20) + '|')
pr('QweRtY'.casefold())
pr('kdfjfnetyf74i65netnt7dunetshe3u87net4yfhd83unet4nnetbrfnet8jns'.count('net'))
pr('kdfjfnetyf74i65netnt7dunetshe3u87net4yfhd83unet4nnetbrfnet8jns'.index('net'))
# raw_tabs = lambda s : [c for c in s]
raw_tabs = lambda s : '|{}|'.format(s.replace('\t', r'\t'))
pr(raw_tabs('tab\ttab\ttab'.expandtabs(2)), raw_tabs('tib\ttib\ttib'.expandtabs(6)), 
raw_tabs('tub\ttub\ttub'.expandtabs(12)), raw_tabs('tob\ttob\ttob'))
pr('isdecimal: ', '123.123'.isdecimal())
pr('isnumeric: ', '123.123'.isnumeric())

lst = [1111,2222,3333]
t  = lst.pop(1)
lst.append(444)
lst.insert(2, 555)
pr(lst, ' > ' , t)

a = (1,2,3)
b = (10,20,30)
c = ('a', 'b', 'c')
pr(tuple(zip(a, b, c))) 
pr(frozenset([1,2,3,4,5,2,3,4,5,6,7]))

printOn = True

def multi_args_long_name_function(*args):
    pr(str(args))

def test_multi():
    var_argument1, var_argument2, var_argument3, var_argument4, var_argument5, var_argument6, var_argument7 = \
    'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg'
    multi_args_long_name_function(var_argument1, var_argument2, 
                                var_argument3, var_argument4, var_argument5, 
                                var_argument6, var_argument7, '001') 
    multi_args_long_name_function(
        var_argument1, var_argument2, var_argument3, 
        var_argument4, var_argument5, var_argument6, 
        var_argument7, '002') 
test_multi()
