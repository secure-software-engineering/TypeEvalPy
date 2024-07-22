#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 46.1:
            return 'lmcde'
        case 'lmcde':
            return 46.1
        case _:
            return "default"


a = func(46.1)
b = func('lmcde')
c = func(8)
