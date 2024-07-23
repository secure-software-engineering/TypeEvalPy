#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (7, 52, 7):
            return 'mkmlj'
        case 'mkmlj':
            return (7, 52, 7)
        case _:
            return "default"


a = func((7, 52, 7))
b = func('mkmlj')
c = func(67)
