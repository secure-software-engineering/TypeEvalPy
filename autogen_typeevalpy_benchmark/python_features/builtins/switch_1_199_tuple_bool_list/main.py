#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (51, 29, 41):
            return True
        case True:
            return (51, 29, 41)
        case _:
            return "default"


a = func((51, 29, 41))
b = func(True)
c = func([97, 59, 12])
