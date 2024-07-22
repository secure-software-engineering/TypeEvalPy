#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 58:
            return True
        case True:
            return 58
        case _:
            return "default"


a = func(58)
b = func(True)
c = func((31, 63, 61))
