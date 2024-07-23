#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (6, 96, 78):
            return True
        case True:
            return (6, 96, 78)
        case _:
            return "default"


a = func((6, 96, 78))
b = func(True)
c = func(88.34)
