#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [95, 95, 28]:
            return 65.9
        case 65.9:
            return [95, 95, 28]
        case _:
            return "default"


a = func([95, 95, 28])
b = func(65.9)
c = func('fgpjp')
