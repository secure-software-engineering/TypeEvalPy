#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 48.33:
            return True
        case True:
            return 48.33
        case _:
            return "default"


a = func(48.33)
b = func(True)
c = func((36, 24, 84))
