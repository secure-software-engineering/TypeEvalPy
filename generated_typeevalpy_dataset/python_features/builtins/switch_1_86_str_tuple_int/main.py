#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'bmwxp':
            return (23, 66, 85)
        case (23, 66, 85):
            return 'bmwxp'
        case _:
            return "default"


a = func('bmwxp')
b = func((23, 66, 85))
c = func(61)
