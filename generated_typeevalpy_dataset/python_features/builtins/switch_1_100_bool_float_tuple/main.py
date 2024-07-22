#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 95.85
        case 95.85:
            return True
        case _:
            return "default"


a = func(True)
b = func(95.85)
c = func((41, 58, 59))
