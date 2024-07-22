#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return (47, 43, 86)
        case (47, 43, 86):
            return True
        case _:
            return "default"


a = func(True)
b = func((47, 43, 86))
c = func('mqkfl')
