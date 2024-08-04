#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'wsica': 54, 'hgkwk': 76, 'hfeuv': 12}:
            return 26.04
        case 26.04:
            return {'wsica': 54, 'hgkwk': 76, 'hfeuv': 12}
        case _:
            return "default"


a = func({'wsica': 54, 'hgkwk': 76, 'hfeuv': 12})
b = func(26.04)
c = func((21, 89, 98))
