#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 13:
            return 37.79
        case 37.79:
            return 13
        case _:
            return "default"


a = func(13)
b = func(37.79)
c = func((2, 69, 5))
