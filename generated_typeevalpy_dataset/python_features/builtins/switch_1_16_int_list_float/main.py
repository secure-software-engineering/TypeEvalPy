#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 47:
            return [83, 21, 48]
        case [83, 21, 48]:
            return 47
        case _:
            return "default"


a = func(47)
b = func([83, 21, 48])
c = func(65.31)
