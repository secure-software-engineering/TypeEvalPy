#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'eboga': 57, 'wlobm': 79, 'ixvgz': 3}:
            return 74
        case 74:
            return {'eboga': 57, 'wlobm': 79, 'ixvgz': 3}
        case _:
            return "default"


a = func({'eboga': 57, 'wlobm': 79, 'ixvgz': 3})
b = func(74)
c = func(True)
