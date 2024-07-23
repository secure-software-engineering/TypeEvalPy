#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 29.74:
            return 'ceooq'
        case 'ceooq':
            return 29.74
        case _:
            return "default"


a = func(29.74)
b = func('ceooq')
c = func(56)
