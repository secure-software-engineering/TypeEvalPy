#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 69:
            return 'wwtex'
        case 'wwtex':
            return 69
        case _:
            return "default"


a = func(69)
b = func('wwtex')
c = func(True)
