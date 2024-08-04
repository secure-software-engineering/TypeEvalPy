#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [53, 78, 59]:
            return (33, 45, 59)
        case (33, 45, 59):
            return [53, 78, 59]
        case _:
            return "default"


a = func([53, 78, 59])
b = func((33, 45, 59))
c = func(91)
