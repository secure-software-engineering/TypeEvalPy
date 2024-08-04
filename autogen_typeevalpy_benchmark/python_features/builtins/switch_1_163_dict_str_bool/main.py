#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'qfsvj': 16, 'utkwh': 60, 'vbhkf': 41}:
            return 'mizbz'
        case 'mizbz':
            return {'qfsvj': 16, 'utkwh': 60, 'vbhkf': 41}
        case _:
            return "default"


a = func({'qfsvj': 16, 'utkwh': 60, 'vbhkf': 41})
b = func('mizbz')
c = func(False)
