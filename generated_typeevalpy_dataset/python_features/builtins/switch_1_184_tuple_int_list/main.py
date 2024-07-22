#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (16, 88, 25):
            return 70
        case 70:
            return (16, 88, 25)
        case _:
            return "default"


a = func((16, 88, 25))
b = func(70)
c = func([87, 10, 1])
