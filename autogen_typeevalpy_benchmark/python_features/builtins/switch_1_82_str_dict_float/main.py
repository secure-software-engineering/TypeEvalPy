#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'ejcvb':
            return {'ggths': 12, 'exuma': 84, 'vzrfd': 86}
        case {'ggths': 12, 'exuma': 84, 'vzrfd': 86}:
            return 'ejcvb'
        case _:
            return "default"


a = func('ejcvb')
b = func({'ggths': 12, 'exuma': 84, 'vzrfd': 86})
c = func(16.33)
