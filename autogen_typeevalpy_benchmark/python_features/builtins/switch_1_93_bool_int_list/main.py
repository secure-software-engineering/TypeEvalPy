#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 19
        case 19:
            return True
        case _:
            return "default"


a = func(True)
b = func(19)
c = func([81, 96, 33])
