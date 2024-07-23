#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [87, 1, 8]:
            return {'rmizh': 58, 'xzsou': 47, 'edyyq': 8}
        case {'rmizh': 58, 'xzsou': 47, 'edyyq': 8}:
            return [87, 1, 8]
        case _:
            return "default"


a = func([87, 1, 8])
b = func({'rmizh': 58, 'xzsou': 47, 'edyyq': 8})
c = func(6)
