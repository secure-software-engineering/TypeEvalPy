#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 87.76:
            return [46, 59, 99]
        case [46, 59, 99]:
            return 87.76
        case _:
            return "default"


a = func(87.76)
b = func([46, 59, 99])
c = func(84)
