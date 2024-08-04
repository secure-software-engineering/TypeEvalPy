#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [55, 38, 12]:
            return 65
        case 65:
            return [55, 38, 12]
        case _:
            return "default"


a = func([55, 38, 12])
b = func(65)
c = func(45.31)
