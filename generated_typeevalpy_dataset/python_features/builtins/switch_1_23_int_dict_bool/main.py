#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 56:
            return {'hmuvy': 76, 'gsucr': 73, 'fqojn': 25}
        case {'hmuvy': 76, 'gsucr': 73, 'fqojn': 25}:
            return 56
        case _:
            return "default"


a = func(56)
b = func({'hmuvy': 76, 'gsucr': 73, 'fqojn': 25})
c = func(False)
