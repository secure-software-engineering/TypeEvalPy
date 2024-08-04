#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (33, 4, 55):
            return 89.64
        case 89.64:
            return (33, 4, 55)
        case _:
            return "default"


a = func((33, 4, 55))
b = func(89.64)
c = func(50)
