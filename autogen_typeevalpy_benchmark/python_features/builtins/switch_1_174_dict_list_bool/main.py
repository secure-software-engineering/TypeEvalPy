#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'vktfb': 15, 'tpeeb': 24, 'goxma': 80}:
            return [45, 78, 3]
        case [45, 78, 3]:
            return {'vktfb': 15, 'tpeeb': 24, 'goxma': 80}
        case _:
            return "default"


a = func({'vktfb': 15, 'tpeeb': 24, 'goxma': 80})
b = func([45, 78, 3])
c = func(True)
