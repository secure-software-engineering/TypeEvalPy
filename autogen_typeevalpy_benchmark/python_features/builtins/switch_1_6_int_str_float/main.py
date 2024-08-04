#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 89:
            return 'edruy'
        case 'edruy':
            return 89
        case _:
            return "default"


a = func(89)
b = func('edruy')
c = func(26.1)
