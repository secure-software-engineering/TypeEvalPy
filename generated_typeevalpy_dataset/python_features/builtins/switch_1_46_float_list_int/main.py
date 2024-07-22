#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 72.52:
            return [2, 40, 81]
        case [2, 40, 81]:
            return 72.52
        case _:
            return "default"


a = func(72.52)
b = func([2, 40, 81])
c = func(48)
