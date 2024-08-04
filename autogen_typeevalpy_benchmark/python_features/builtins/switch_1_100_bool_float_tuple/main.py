#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 85.15
        case 85.15:
            return True
        case _:
            return "default"


a = func(True)
b = func(85.15)
c = func((88, 36, 4))
