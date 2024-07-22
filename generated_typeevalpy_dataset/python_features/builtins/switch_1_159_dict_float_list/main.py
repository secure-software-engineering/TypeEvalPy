#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ooumw': 44, 'qhvwl': 6, 'cxing': 10}:
            return 56.67
        case 56.67:
            return {'ooumw': 44, 'qhvwl': 6, 'cxing': 10}
        case _:
            return "default"


a = func({'ooumw': 44, 'qhvwl': 6, 'cxing': 10})
b = func(56.67)
c = func([53, 25, 12])
