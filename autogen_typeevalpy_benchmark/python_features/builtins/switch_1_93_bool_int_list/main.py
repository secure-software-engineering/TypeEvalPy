#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 48
        case 48:
            return True
        case _:
            return "default"


a = func(True)
b = func(48)
c = func([89, 1, 3])
