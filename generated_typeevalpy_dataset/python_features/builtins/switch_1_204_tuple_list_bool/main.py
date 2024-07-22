#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (72, 85, 20):
            return [74, 97, 33]
        case [74, 97, 33]:
            return (72, 85, 20)
        case _:
            return "default"


a = func((72, 85, 20))
b = func([74, 97, 33])
c = func(True)
