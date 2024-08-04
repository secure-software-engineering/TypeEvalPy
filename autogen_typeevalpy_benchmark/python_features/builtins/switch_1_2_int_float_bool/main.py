#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 49:
            return 89.31
        case 89.31:
            return 49
        case _:
            return "default"


a = func(49)
b = func(89.31)
c = func(False)
