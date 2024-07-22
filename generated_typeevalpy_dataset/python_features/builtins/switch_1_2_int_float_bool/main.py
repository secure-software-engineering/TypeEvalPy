#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 36:
            return 30.12
        case 30.12:
            return 36
        case _:
            return "default"


a = func(36)
b = func(30.12)
c = func(True)
