#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return (87, 38, 90)
        case (87, 38, 90):
            return True
        case _:
            return "default"


a = func(True)
b = func((87, 38, 90))
c = func(98)
