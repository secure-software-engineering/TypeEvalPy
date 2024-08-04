#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 83.53:
            return 81
        case 81:
            return 83.53
        case _:
            return "default"


a = func(83.53)
b = func(81)
c = func((32, 100, 21))
