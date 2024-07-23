#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 94:
            return (16, 16, 11)
        case (16, 16, 11):
            return 94
        case _:
            return "default"


a = func(94)
b = func((16, 16, 11))
c = func(True)
