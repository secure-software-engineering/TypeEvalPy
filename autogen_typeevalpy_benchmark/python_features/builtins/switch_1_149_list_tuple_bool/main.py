#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [72, 37, 32]:
            return (2, 72, 62)
        case (2, 72, 62):
            return [72, 37, 32]
        case _:
            return "default"


a = func([72, 37, 32])
b = func((2, 72, 62))
c = func(True)
