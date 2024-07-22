#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 62.74:
            return 'lleda'
        case 'lleda':
            return 62.74
        case _:
            return "default"


a = func(62.74)
b = func('lleda')
c = func([84, 34, 6])
