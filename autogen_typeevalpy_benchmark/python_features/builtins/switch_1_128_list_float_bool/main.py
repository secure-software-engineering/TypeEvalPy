#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [20, 96, 91]:
            return 27.67
        case 27.67:
            return [20, 96, 91]
        case _:
            return "default"


a = func([20, 96, 91])
b = func(27.67)
c = func(True)
