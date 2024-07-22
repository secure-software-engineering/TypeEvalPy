#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 33.59:
            return (3, 33, 82)
        case (3, 33, 82):
            return 33.59
        case _:
            return "default"


a = func(33.59)
b = func((3, 33, 82))
c = func([34, 40, 78])
