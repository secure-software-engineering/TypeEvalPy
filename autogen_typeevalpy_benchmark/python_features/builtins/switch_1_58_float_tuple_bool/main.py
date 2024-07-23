#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 86.32:
            return (50, 24, 44)
        case (50, 24, 44):
            return 86.32
        case _:
            return "default"


a = func(86.32)
b = func((50, 24, 44))
c = func(False)
