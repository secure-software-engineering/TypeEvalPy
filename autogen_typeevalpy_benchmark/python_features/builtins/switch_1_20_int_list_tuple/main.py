#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 58:
            return [51, 18, 22]
        case [51, 18, 22]:
            return 58
        case _:
            return "default"


a = func(58)
b = func([51, 18, 22])
c = func((40, 56, 13))
