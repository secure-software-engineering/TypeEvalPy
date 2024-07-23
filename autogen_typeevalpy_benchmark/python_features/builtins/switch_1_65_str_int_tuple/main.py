#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'xofoe':
            return 78
        case 78:
            return 'xofoe'
        case _:
            return "default"


a = func('xofoe')
b = func(78)
c = func((5, 55, 27))
