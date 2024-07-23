#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [94, 21, 70]:
            return (12, 66, 48)
        case (12, 66, 48):
            return [94, 21, 70]
        case _:
            return "default"


a = func([94, 21, 70])
b = func((12, 66, 48))
c = func(70.49)
