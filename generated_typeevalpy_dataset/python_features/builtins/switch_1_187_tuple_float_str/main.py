#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (41, 35, 37):
            return 43.77
        case 43.77:
            return (41, 35, 37)
        case _:
            return "default"


a = func((41, 35, 37))
b = func(43.77)
c = func('sylzp')
