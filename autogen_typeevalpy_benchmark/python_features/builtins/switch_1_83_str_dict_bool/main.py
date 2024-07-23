#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'xozwc':
            return {'tiehl': 78, 'guazj': 91, 'zctqz': 36}
        case {'tiehl': 78, 'guazj': 91, 'zctqz': 36}:
            return 'xozwc'
        case _:
            return "default"


a = func('xozwc')
b = func({'tiehl': 78, 'guazj': 91, 'zctqz': 36})
c = func(True)
