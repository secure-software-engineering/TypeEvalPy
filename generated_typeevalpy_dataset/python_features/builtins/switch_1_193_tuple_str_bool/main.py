#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (88, 38, 73):
            return 'bmxki'
        case 'bmxki':
            return (88, 38, 73)
        case _:
            return "default"


a = func((88, 38, 73))
b = func('bmxki')
c = func(True)
