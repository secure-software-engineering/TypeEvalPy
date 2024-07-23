#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 1.85:
            return 67
        case 67:
            return 1.85
        case _:
            return "default"


a = func(1.85)
b = func(67)
c = func((17, 60, 51))
