#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'vptpl':
            return 67.75
        case 67.75:
            return 'vptpl'
        case _:
            return "default"


a = func('vptpl')
b = func(67.75)
c = func((41, 33, 4))
