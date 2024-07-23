#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 99.53
        case 99.53:
            return True
        case _:
            return "default"


a = func(True)
b = func(99.53)
c = func((80, 92, 6))
