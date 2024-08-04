#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 31:
            return 33.61
        case 33.61:
            return 31
        case _:
            return "default"


a = func(31)
b = func(33.61)
c = func((43, 23, 55))
