#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [69, 60, 87]:
            return {'gnuhb': 12, 'udkyf': 70, 'aewgb': 90}
        case {'gnuhb': 12, 'udkyf': 70, 'aewgb': 90}:
            return [69, 60, 87]
        case _:
            return "default"


a = func([69, 60, 87])
b = func({'gnuhb': 12, 'udkyf': 70, 'aewgb': 90})
c = func(True)
