#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [7, 100, 100]:
            return 94.11
        case 94.11:
            return [7, 100, 100]
        case _:
            return "default"


a = func([7, 100, 100])
b = func(94.11)
c = func(29)
