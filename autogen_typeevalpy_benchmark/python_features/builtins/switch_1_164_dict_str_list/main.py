#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'cszkr': 30, 'jvjpi': 91, 'kbyxx': 29}:
            return 'lievt'
        case 'lievt':
            return {'cszkr': 30, 'jvjpi': 91, 'kbyxx': 29}
        case _:
            return "default"


a = func({'cszkr': 30, 'jvjpi': 91, 'kbyxx': 29})
b = func('lievt')
c = func([67, 33, 82])
