#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 27:
            return {'kmprl': 52, 'jlrjg': 2, 'elezw': 29}
        case {'kmprl': 52, 'jlrjg': 2, 'elezw': 29}:
            return 27
        case _:
            return "default"


a = func(27)
b = func({'kmprl': 52, 'jlrjg': 2, 'elezw': 29})
c = func([24, 75, 2])
