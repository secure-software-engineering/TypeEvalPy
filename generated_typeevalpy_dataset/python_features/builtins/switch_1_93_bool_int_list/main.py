#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 52
        case 52:
            return True
        case _:
            return "default"


a = func(True)
b = func(52)
c = func([55, 28, 75])
