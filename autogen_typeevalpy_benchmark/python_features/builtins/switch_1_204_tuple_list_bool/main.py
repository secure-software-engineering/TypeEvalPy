#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (54, 28, 52):
            return [22, 68, 72]
        case [22, 68, 72]:
            return (54, 28, 52)
        case _:
            return "default"


a = func((54, 28, 52))
b = func([22, 68, 72])
c = func(False)
