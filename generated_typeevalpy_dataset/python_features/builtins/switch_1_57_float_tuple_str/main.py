#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 36.61:
            return (69, 45, 96)
        case (69, 45, 96):
            return 36.61
        case _:
            return "default"


a = func(36.61)
b = func((69, 45, 96))
c = func('qpmfp')
