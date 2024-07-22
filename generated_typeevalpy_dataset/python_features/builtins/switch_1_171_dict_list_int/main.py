#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'odkod': 27, 'bmgjm': 93, 'mgeeg': 97}:
            return [18, 85, 72]
        case [18, 85, 72]:
            return {'odkod': 27, 'bmgjm': 93, 'mgeeg': 97}
        case _:
            return "default"


a = func({'odkod': 27, 'bmgjm': 93, 'mgeeg': 97})
b = func([18, 85, 72])
c = func(82)
