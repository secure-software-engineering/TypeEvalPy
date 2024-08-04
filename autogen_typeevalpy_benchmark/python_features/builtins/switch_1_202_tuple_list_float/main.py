#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (14, 53, 55):
            return [25, 32, 35]
        case [25, 32, 35]:
            return (14, 53, 55)
        case _:
            return "default"


a = func((14, 53, 55))
b = func([25, 32, 35])
c = func(78.17)
