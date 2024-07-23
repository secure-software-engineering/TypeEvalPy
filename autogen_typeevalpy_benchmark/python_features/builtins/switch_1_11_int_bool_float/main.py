#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 63:
            return True
        case True:
            return 63
        case _:
            return "default"


a = func(63)
b = func(True)
c = func(9.51)
