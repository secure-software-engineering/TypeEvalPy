#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 29:
            return (56, 13, 14)
        case (56, 13, 14):
            return 29
        case _:
            return "default"


a = func(29)
b = func((56, 13, 14))
c = func([35, 66, 55])
