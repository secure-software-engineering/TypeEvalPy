#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (37, 96, 50):
            return True
        case True:
            return (37, 96, 50)
        case _:
            return "default"


a = func((37, 96, 50))
b = func(True)
c = func(97)
