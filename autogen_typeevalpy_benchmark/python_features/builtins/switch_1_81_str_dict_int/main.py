#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'npdko':
            return {'hawdy': 48, 'rbnth': 13, 'dcgjj': 66}
        case {'hawdy': 48, 'rbnth': 13, 'dcgjj': 66}:
            return 'npdko'
        case _:
            return "default"


a = func('npdko')
b = func({'hawdy': 48, 'rbnth': 13, 'dcgjj': 66})
c = func(16)
