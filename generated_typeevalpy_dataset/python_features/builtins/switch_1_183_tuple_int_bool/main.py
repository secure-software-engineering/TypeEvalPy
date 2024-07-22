#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (50, 91, 35):
            return 97
        case 97:
            return (50, 91, 35)
        case _:
            return "default"


a = func((50, 91, 35))
b = func(97)
c = func(False)
