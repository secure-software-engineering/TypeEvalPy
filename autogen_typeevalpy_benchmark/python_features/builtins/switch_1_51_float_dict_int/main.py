#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 8.0:
            return {'oaipb': 25, 'ughjt': 91, 'ejicv': 5}
        case {'oaipb': 25, 'ughjt': 91, 'ejicv': 5}:
            return 8.0
        case _:
            return "default"


a = func(8.0)
b = func({'oaipb': 25, 'ughjt': 91, 'ejicv': 5})
c = func(96)
