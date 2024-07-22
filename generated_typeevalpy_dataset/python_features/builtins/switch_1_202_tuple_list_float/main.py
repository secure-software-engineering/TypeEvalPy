#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (47, 1, 80):
            return [24, 49, 3]
        case [24, 49, 3]:
            return (47, 1, 80)
        case _:
            return "default"


a = func((47, 1, 80))
b = func([24, 49, 3])
c = func(91.44)
