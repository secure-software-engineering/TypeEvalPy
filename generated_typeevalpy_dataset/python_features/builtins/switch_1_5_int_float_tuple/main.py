#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 38:
            return 37.12
        case 37.12:
            return 38
        case _:
            return "default"


a = func(38)
b = func(37.12)
c = func((22, 23, 60))
