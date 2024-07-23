#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 24:
            return 'fihjz'
        case 'fihjz':
            return 24
        case _:
            return "default"


a = func(24)
b = func('fihjz')
c = func(85.41)
