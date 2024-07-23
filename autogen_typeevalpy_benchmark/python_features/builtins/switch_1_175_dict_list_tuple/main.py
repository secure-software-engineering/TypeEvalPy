#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'yjgxv': 84, 'tfxpz': 17, 'ujarb': 93}:
            return [19, 31, 65]
        case [19, 31, 65]:
            return {'yjgxv': 84, 'tfxpz': 17, 'ujarb': 93}
        case _:
            return "default"


a = func({'yjgxv': 84, 'tfxpz': 17, 'ujarb': 93})
b = func([19, 31, 65])
c = func((54, 91, 16))
