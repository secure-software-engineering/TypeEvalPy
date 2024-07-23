#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 23.77:
            return [98, 34, 11]
        case [98, 34, 11]:
            return 23.77
        case _:
            return "default"


a = func(23.77)
b = func([98, 34, 11])
c = func((5, 56, 86))
