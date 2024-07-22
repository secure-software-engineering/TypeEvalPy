#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 32.95:
            return 66
        case 66:
            return 32.95
        case _:
            return "default"


a = func(32.95)
b = func(66)
c = func((83, 78, 25))
