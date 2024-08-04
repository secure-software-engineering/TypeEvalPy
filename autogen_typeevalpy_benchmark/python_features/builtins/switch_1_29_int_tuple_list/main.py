#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 58:
            return (39, 6, 20)
        case (39, 6, 20):
            return 58
        case _:
            return "default"


a = func(58)
b = func((39, 6, 20))
c = func([7, 80, 65])
