#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'nusym':
            return (54, 4, 73)
        case (54, 4, 73):
            return 'nusym'
        case _:
            return "default"


a = func('nusym')
b = func((54, 4, 73))
c = func(6)
