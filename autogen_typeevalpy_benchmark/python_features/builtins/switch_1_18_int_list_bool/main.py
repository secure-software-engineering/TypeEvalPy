#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 1:
            return [14, 68, 10]
        case [14, 68, 10]:
            return 1
        case _:
            return "default"


a = func(1)
b = func([14, 68, 10])
c = func(False)
