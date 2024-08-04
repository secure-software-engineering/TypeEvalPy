#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (64, 65, 33):
            return 56
        case 56:
            return (64, 65, 33)
        case _:
            return "default"


a = func((64, 65, 33))
b = func(56)
c = func('lmtos')
