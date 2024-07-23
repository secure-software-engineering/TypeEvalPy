#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 38:
            return 'mnewb'
        case 'mnewb':
            return 38
        case _:
            return "default"


a = func(38)
b = func('mnewb')
c = func([31, 97, 68])
