#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'cuzmv': 30, 'ntyai': 100, 'inwtl': 3}:
            return (22, 22, 6)
        case (22, 22, 6):
            return {'cuzmv': 30, 'ntyai': 100, 'inwtl': 3}
        case _:
            return "default"


a = func({'cuzmv': 30, 'ntyai': 100, 'inwtl': 3})
b = func((22, 22, 6))
c = func(False)
