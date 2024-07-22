#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [6, 56, 50]:
            return 98.51
        case 98.51:
            return [6, 56, 50]
        case _:
            return "default"


a = func([6, 56, 50])
b = func(98.51)
c = func(84)
