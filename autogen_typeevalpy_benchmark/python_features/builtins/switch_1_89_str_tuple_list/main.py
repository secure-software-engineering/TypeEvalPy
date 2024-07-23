#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'pnskf':
            return (37, 66, 53)
        case (37, 66, 53):
            return 'pnskf'
        case _:
            return "default"


a = func('pnskf')
b = func((37, 66, 53))
c = func([72, 29, 96])
