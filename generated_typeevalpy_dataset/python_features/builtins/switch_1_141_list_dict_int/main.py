#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [32, 68, 1]:
            return {'xhrum': 21, 'dgouj': 41, 'roouu': 3}
        case {'xhrum': 21, 'dgouj': 41, 'roouu': 3}:
            return [32, 68, 1]
        case _:
            return "default"


a = func([32, 68, 1])
b = func({'xhrum': 21, 'dgouj': 41, 'roouu': 3})
c = func(24)
