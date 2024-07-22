#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [12, 21, 63]:
            return 48
        case 48:
            return [12, 21, 63]
        case _:
            return "default"


a = func([12, 21, 63])
b = func(48)
c = func(False)
