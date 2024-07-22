#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return (70, 82, 63)
        case (70, 82, 63):
            return True
        case _:
            return "default"


a = func(True)
b = func((70, 82, 63))
c = func(92.84)
