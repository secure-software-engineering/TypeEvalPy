#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 47
        case 47:
            return True
        case _:
            return "default"


a = func(True)
b = func(47)
c = func(26.07)
