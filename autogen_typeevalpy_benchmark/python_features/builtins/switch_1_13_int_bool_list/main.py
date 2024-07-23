#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 49:
            return True
        case True:
            return 49
        case _:
            return "default"


a = func(49)
b = func(True)
c = func([47, 76, 88])
