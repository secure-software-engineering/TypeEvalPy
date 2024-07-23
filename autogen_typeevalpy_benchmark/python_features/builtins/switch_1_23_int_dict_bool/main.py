#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 42:
            return {'kgnzz': 21, 'ycsez': 25, 'ewmrb': 51}
        case {'kgnzz': 21, 'ycsez': 25, 'ewmrb': 51}:
            return 42
        case _:
            return "default"


a = func(42)
b = func({'kgnzz': 21, 'ycsez': 25, 'ewmrb': 51})
c = func(True)
