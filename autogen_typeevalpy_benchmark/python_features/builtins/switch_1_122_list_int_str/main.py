#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [18, 15, 4]:
            return 49
        case 49:
            return [18, 15, 4]
        case _:
            return "default"


a = func([18, 15, 4])
b = func(49)
c = func('khjwv')
