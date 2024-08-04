#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [86, 93, 21]:
            return 47.49
        case 47.49:
            return [86, 93, 21]
        case _:
            return "default"


a = func([86, 93, 21])
b = func(47.49)
c = func('fimdk')
