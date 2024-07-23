#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 27:
            return [13, 82, 70]
        case [13, 82, 70]:
            return 27
        case _:
            return "default"


a = func(27)
b = func([13, 82, 70])
c = func(88.79)
