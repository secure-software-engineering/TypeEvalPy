#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 36.58:
            return {'oeoyw': 30, 'wselv': 28, 'dfwcr': 23}
        case {'oeoyw': 30, 'wselv': 28, 'dfwcr': 23}:
            return 36.58
        case _:
            return "default"


a = func(36.58)
b = func({'oeoyw': 30, 'wselv': 28, 'dfwcr': 23})
c = func(False)
