#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'odgku': 86, 'mjetm': 92, 'xmuuh': 83}:
            return [40, 5, 51]
        case [40, 5, 51]:
            return {'odgku': 86, 'mjetm': 92, 'xmuuh': 83}
        case _:
            return "default"


a = func({'odgku': 86, 'mjetm': 92, 'xmuuh': 83})
b = func([40, 5, 51])
c = func(True)
