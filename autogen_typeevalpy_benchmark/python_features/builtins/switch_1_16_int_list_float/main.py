#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 9:
            return [3, 39, 19]
        case [3, 39, 19]:
            return 9
        case _:
            return "default"


a = func(9)
b = func([3, 39, 19])
c = func(85.95)
