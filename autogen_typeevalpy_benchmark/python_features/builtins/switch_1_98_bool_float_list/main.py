#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 56.01
        case 56.01:
            return True
        case _:
            return "default"


a = func(True)
b = func(56.01)
c = func([81, 23, 70])
