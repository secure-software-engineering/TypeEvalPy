#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'sxyar':
            return {'dnvxh': 25, 'utnkn': 6, 'bdpri': 49}
        case {'dnvxh': 25, 'utnkn': 6, 'bdpri': 49}:
            return 'sxyar'
        case _:
            return "default"


a = func('sxyar')
b = func({'dnvxh': 25, 'utnkn': 6, 'bdpri': 49})
c = func(80)
