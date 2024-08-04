#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [21, 36, 74]:
            return 28
        case 28:
            return [21, 36, 74]
        case _:
            return "default"


a = func([21, 36, 74])
b = func(28)
c = func(True)
