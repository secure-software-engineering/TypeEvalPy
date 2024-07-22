#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (25, 24, 66):
            return True
        case True:
            return (25, 24, 66)
        case _:
            return "default"


a = func((25, 24, 66))
b = func(True)
c = func({'pbryc': 62, 'eltze': 74, 'epqoc': 51})
