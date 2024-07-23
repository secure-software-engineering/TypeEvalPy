#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 29:
            return 34.13
        case 34.13:
            return 29
        case _:
            return "default"


a = func(29)
b = func(34.13)
c = func(False)
