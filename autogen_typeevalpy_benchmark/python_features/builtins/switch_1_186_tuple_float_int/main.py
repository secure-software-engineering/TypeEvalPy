#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (62, 25, 77):
            return 58.85
        case 58.85:
            return (62, 25, 77)
        case _:
            return "default"


a = func((62, 25, 77))
b = func(58.85)
c = func(56)
