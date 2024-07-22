#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'gwebt': 89, 'tvvco': 40, 'icrmz': 91}:
            return True
        case True:
            return {'gwebt': 89, 'tvvco': 40, 'icrmz': 91}
        case _:
            return "default"


a = func({'gwebt': 89, 'tvvco': 40, 'icrmz': 91})
b = func(True)
c = func((44, 19, 61))
