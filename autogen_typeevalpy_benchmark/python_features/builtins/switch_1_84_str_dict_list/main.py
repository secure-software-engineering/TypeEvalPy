#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'tjfgd':
            return {'udvcr': 27, 'rqsit': 57, 'ksnwi': 98}
        case {'udvcr': 27, 'rqsit': 57, 'ksnwi': 98}:
            return 'tjfgd'
        case _:
            return "default"


a = func('tjfgd')
b = func({'udvcr': 27, 'rqsit': 57, 'ksnwi': 98})
c = func([100, 41, 69])
