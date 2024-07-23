#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (66, 32, 86):
            return 7
        case 7:
            return (66, 32, 86)
        case _:
            return "default"


a = func((66, 32, 86))
b = func(7)
c = func(46.75)
