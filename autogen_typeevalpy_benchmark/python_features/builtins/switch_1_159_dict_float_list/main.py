#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'fxrcz': 54, 'jgsjm': 87, 'xyuct': 24}:
            return 98.32
        case 98.32:
            return {'fxrcz': 54, 'jgsjm': 87, 'xyuct': 24}
        case _:
            return "default"


a = func({'fxrcz': 54, 'jgsjm': 87, 'xyuct': 24})
b = func(98.32)
c = func([5, 91, 51])
