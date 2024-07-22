#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 40.92:
            return 73
        case 73:
            return 40.92
        case _:
            return "default"


a = func(40.92)
b = func(73)
c = func([86, 28, 29])
