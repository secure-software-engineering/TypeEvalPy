#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'jatba':
            return {'orgkz': 86, 'fttqw': 28, 'pkxfh': 11}
        case {'orgkz': 86, 'fttqw': 28, 'pkxfh': 11}:
            return 'jatba'
        case _:
            return "default"


a = func('jatba')
b = func({'orgkz': 86, 'fttqw': 28, 'pkxfh': 11})
c = func(True)
