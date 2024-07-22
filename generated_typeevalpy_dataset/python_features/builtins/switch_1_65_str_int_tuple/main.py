#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'bdfyt':
            return 78
        case 78:
            return 'bdfyt'
        case _:
            return "default"


a = func('bdfyt')
b = func(78)
c = func((72, 18, 47))
