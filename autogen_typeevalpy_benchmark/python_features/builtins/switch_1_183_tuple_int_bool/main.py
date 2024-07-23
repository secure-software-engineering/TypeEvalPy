#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (15, 33, 78):
            return 99
        case 99:
            return (15, 33, 78)
        case _:
            return "default"


a = func((15, 33, 78))
b = func(99)
c = func(False)
