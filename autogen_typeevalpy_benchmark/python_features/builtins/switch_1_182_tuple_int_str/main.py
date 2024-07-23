#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (33, 98, 15):
            return 46
        case 46:
            return (33, 98, 15)
        case _:
            return "default"


a = func((33, 98, 15))
b = func(46)
c = func('evcah')
