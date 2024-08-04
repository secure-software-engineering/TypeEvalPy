#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (31, 40, 1):
            return [50, 81, 21]
        case [50, 81, 21]:
            return (31, 40, 1)
        case _:
            return "default"


a = func((31, 40, 1))
b = func([50, 81, 21])
c = func(8)
