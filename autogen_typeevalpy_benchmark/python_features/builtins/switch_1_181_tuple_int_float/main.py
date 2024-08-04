#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (53, 63, 58):
            return 8
        case 8:
            return (53, 63, 58)
        case _:
            return "default"


a = func((53, 63, 58))
b = func(8)
c = func(24.04)
