#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 72:
            return 41.55
        case 41.55:
            return 72
        case _:
            return "default"


a = func(72)
b = func(41.55)
c = func([25, 74, 80])
