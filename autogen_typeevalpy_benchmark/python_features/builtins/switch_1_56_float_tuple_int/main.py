#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 3.65:
            return (69, 13, 66)
        case (69, 13, 66):
            return 3.65
        case _:
            return "default"


a = func(3.65)
b = func((69, 13, 66))
c = func(3)
