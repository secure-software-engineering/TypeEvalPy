#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 76:
            return [16, 59, 8]
        case [16, 59, 8]:
            return 76
        case _:
            return "default"


a = func(76)
b = func([16, 59, 8])
c = func((67, 88, 50))
