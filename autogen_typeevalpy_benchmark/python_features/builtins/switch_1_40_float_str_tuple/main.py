#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 59.77:
            return 'lbozj'
        case 'lbozj':
            return 59.77
        case _:
            return "default"


a = func(59.77)
b = func('lbozj')
c = func((72, 93, 38))
