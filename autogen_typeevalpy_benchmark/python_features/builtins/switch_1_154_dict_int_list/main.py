#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'kgdgc': 27, 'mvizt': 76, 'wejlc': 23}:
            return 3
        case 3:
            return {'kgdgc': 27, 'mvizt': 76, 'wejlc': 23}
        case _:
            return "default"


a = func({'kgdgc': 27, 'mvizt': 76, 'wejlc': 23})
b = func(3)
c = func([4, 84, 76])
