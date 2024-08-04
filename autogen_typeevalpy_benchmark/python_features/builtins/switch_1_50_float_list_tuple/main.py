#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 46.15:
            return [65, 54, 91]
        case [65, 54, 91]:
            return 46.15
        case _:
            return "default"


a = func(46.15)
b = func([65, 54, 91])
c = func((54, 17, 99))
