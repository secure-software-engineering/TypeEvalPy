#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 83.56:
            return (88, 44, 9)
        case (88, 44, 9):
            return 83.56
        case _:
            return "default"


a = func(83.56)
b = func((88, 44, 9))
c = func([1, 85, 98])
