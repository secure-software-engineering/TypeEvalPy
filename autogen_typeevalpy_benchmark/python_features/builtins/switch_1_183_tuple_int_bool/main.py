#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (4, 84, 58):
            return 51
        case 51:
            return (4, 84, 58)
        case _:
            return "default"


a = func((4, 84, 58))
b = func(51)
c = func(False)
