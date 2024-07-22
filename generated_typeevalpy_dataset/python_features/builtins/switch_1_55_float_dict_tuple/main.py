#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 13.67:
            return {'jifkd': 36, 'dtypw': 50, 'zrtmh': 51}
        case {'jifkd': 36, 'dtypw': 50, 'zrtmh': 51}:
            return 13.67
        case _:
            return "default"


a = func(13.67)
b = func({'jifkd': 36, 'dtypw': 50, 'zrtmh': 51})
c = func((39, 70, 4))
