#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'fgkne': 58, 'fnppt': 59, 'zlosc': 64}:
            return 'wztxl'
        case 'wztxl':
            return {'fgkne': 58, 'fnppt': 59, 'zlosc': 64}
        case _:
            return "default"


a = func({'fgkne': 58, 'fnppt': 59, 'zlosc': 64})
b = func('wztxl')
c = func(17.38)
