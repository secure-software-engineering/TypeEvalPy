#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'nksab': 24, 'darmw': 32, 'ydpth': 77}
        case {'nksab': 24, 'darmw': 32, 'ydpth': 77}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'nksab': 24, 'darmw': 32, 'ydpth': 77})
c = func(99.6)
