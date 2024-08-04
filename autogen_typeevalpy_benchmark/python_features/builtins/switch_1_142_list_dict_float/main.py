#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [57, 84, 52]:
            return {'murlv': 95, 'yvskw': 44, 'mkodn': 83}
        case {'murlv': 95, 'yvskw': 44, 'mkodn': 83}:
            return [57, 84, 52]
        case _:
            return "default"


a = func([57, 84, 52])
b = func({'murlv': 95, 'yvskw': 44, 'mkodn': 83})
c = func(14.83)
