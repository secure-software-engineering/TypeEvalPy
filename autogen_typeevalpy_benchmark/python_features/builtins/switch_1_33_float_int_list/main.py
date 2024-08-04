#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 89.35:
            return 13
        case 13:
            return 89.35
        case _:
            return "default"


a = func(89.35)
b = func(13)
c = func([25, 8, 67])
