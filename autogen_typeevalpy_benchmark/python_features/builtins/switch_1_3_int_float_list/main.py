#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 82:
            return 58.22
        case 58.22:
            return 82
        case _:
            return "default"


a = func(82)
b = func(58.22)
c = func([20, 49, 63])
