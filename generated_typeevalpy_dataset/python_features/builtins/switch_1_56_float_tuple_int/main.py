#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 61.31:
            return (21, 41, 33)
        case (21, 41, 33):
            return 61.31
        case _:
            return "default"


a = func(61.31)
b = func((21, 41, 33))
c = func(52)
