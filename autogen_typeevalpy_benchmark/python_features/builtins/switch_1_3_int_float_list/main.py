#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 23:
            return 72.32
        case 72.32:
            return 23
        case _:
            return "default"


a = func(23)
b = func(72.32)
c = func([37, 27, 99])
