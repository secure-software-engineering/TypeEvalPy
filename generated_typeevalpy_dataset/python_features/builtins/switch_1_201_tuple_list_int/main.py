#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (98, 2, 98):
            return [7, 19, 62]
        case [7, 19, 62]:
            return (98, 2, 98)
        case _:
            return "default"


a = func((98, 2, 98))
b = func([7, 19, 62])
c = func(81)
