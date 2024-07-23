#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 88.43:
            return [96, 97, 71]
        case [96, 97, 71]:
            return 88.43
        case _:
            return "default"


a = func(88.43)
b = func([96, 97, 71])
c = func('mfltw')
