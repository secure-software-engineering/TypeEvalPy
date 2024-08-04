#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 62.29:
            return 'tqqrp'
        case 'tqqrp':
            return 62.29
        case _:
            return "default"


a = func(62.29)
b = func('tqqrp')
c = func([69, 64, 82])
