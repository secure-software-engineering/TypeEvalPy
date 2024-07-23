#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return (84, 64, 65)
        case (84, 64, 65):
            return True
        case _:
            return "default"


a = func(True)
b = func((84, 64, 65))
c = func(84.61)
