#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 15.8:
            return 15
        case 15:
            return 15.8
        case _:
            return "default"


a = func(15.8)
b = func(15)
c = func(True)
