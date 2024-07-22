#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [35, 83, 4]:
            return 17
        case 17:
            return [35, 83, 4]
        case _:
            return "default"


a = func([35, 83, 4])
b = func(17)
c = func((21, 23, 79))
