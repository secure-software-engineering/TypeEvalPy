#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'pnfzz':
            return 41.89
        case 41.89:
            return 'pnfzz'
        case _:
            return "default"


a = func('pnfzz')
b = func(41.89)
c = func([15, 83, 96])
