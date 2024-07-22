#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 76.51:
            return 70
        case 70:
            return 76.51
        case _:
            return "default"


a = func(76.51)
b = func(70)
c = func(False)
