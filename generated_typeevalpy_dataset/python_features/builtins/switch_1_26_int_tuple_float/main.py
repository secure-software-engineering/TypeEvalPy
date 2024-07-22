#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 31:
            return (67, 13, 44)
        case (67, 13, 44):
            return 31
        case _:
            return "default"


a = func(31)
b = func((67, 13, 44))
c = func(76.66)
