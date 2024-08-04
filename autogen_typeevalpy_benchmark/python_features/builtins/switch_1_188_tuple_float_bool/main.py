#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (9, 87, 61):
            return 64.17
        case 64.17:
            return (9, 87, 61)
        case _:
            return "default"


a = func((9, 87, 61))
b = func(64.17)
c = func(False)
