#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 89:
            return (99, 11, 48)
        case (99, 11, 48):
            return 89
        case _:
            return "default"


a = func(89)
b = func((99, 11, 48))
c = func('qmeqw')
