#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 50.58:
            return (39, 10, 91)
        case (39, 10, 91):
            return 50.58
        case _:
            return "default"


a = func(50.58)
b = func((39, 10, 91))
c = func(False)
