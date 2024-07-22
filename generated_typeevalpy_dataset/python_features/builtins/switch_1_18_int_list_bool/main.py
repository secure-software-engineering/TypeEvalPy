#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 22:
            return [51, 74, 91]
        case [51, 74, 91]:
            return 22
        case _:
            return "default"


a = func(22)
b = func([51, 74, 91])
c = func(False)
