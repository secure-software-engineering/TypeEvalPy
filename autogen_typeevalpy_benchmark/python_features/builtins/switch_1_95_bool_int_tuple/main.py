#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 40
        case 40:
            return True
        case _:
            return "default"


a = func(True)
b = func(40)
c = func((38, 38, 58))
