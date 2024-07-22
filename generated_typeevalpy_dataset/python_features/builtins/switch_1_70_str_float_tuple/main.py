#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'smeyc':
            return 97.3
        case 97.3:
            return 'smeyc'
        case _:
            return "default"


a = func('smeyc')
b = func(97.3)
c = func((79, 76, 73))
