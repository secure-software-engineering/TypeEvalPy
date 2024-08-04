#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 59.72:
            return [87, 11, 84]
        case [87, 11, 84]:
            return 59.72
        case _:
            return "default"


a = func(59.72)
b = func([87, 11, 84])
c = func(True)
