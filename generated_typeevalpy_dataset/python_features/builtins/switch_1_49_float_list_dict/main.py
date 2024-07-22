#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 37.65:
            return [62, 44, 48]
        case [62, 44, 48]:
            return 37.65
        case _:
            return "default"


a = func(37.65)
b = func([62, 44, 48])
c = func({'ahkwl': 76, 'dvvmz': 8, 'nyxtq': 77})
