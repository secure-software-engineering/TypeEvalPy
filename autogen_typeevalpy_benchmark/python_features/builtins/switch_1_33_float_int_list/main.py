#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 34.81:
            return 69
        case 69:
            return 34.81
        case _:
            return "default"


a = func(34.81)
b = func(69)
c = func([9, 45, 20])
