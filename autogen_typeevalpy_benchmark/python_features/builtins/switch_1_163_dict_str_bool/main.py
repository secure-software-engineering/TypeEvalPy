#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'hwklq': 5, 'usqki': 27, 'pfgpr': 98}:
            return 'fczll'
        case 'fczll':
            return {'hwklq': 5, 'usqki': 27, 'pfgpr': 98}
        case _:
            return "default"


a = func({'hwklq': 5, 'usqki': 27, 'pfgpr': 98})
b = func('fczll')
c = func(False)
