#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [73, 31, 31]:
            return {'vxccw': 51, 'gajni': 14, 'nidhd': 44}
        case {'vxccw': 51, 'gajni': 14, 'nidhd': 44}:
            return [73, 31, 31]
        case _:
            return "default"


a = func([73, 31, 31])
b = func({'vxccw': 51, 'gajni': 14, 'nidhd': 44})
c = func((10, 36, 25))
