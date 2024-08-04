#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 33.41:
            return {'bhpfr': 55, 'ctycp': 30, 'mirzu': 52}
        case {'bhpfr': 55, 'ctycp': 30, 'mirzu': 52}:
            return 33.41
        case _:
            return "default"


a = func(33.41)
b = func({'bhpfr': 55, 'ctycp': 30, 'mirzu': 52})
c = func('ttawt')
