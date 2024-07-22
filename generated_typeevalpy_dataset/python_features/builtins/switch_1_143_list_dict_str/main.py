#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [11, 91, 5]:
            return {'ekwib': 65, 'zixso': 37, 'rmilr': 26}
        case {'ekwib': 65, 'zixso': 37, 'rmilr': 26}:
            return [11, 91, 5]
        case _:
            return "default"


a = func([11, 91, 5])
b = func({'ekwib': 65, 'zixso': 37, 'rmilr': 26})
c = func('lvoac')
