#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [38, 94, 4]:
            return 48
        case 48:
            return [38, 94, 4]
        case _:
            return "default"


a = func([38, 94, 4])
b = func(48)
c = func(70.79)
