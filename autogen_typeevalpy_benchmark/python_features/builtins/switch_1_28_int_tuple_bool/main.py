#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 16:
            return (21, 91, 4)
        case (21, 91, 4):
            return 16
        case _:
            return "default"


a = func(16)
b = func((21, 91, 4))
c = func(True)
