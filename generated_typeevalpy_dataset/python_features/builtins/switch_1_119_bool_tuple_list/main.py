#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return (19, 43, 26)
        case (19, 43, 26):
            return True
        case _:
            return "default"


a = func(True)
b = func((19, 43, 26))
c = func([10, 94, 82])
