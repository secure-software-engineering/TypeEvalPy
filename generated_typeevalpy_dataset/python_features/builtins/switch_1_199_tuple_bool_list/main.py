#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (40, 38, 78):
            return True
        case True:
            return (40, 38, 78)
        case _:
            return "default"


a = func((40, 38, 78))
b = func(True)
c = func([29, 90, 4])
