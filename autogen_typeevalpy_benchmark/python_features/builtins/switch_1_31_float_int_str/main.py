#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 79.54:
            return 55
        case 55:
            return 79.54
        case _:
            return "default"


a = func(79.54)
b = func(55)
c = func('ymmeq')
