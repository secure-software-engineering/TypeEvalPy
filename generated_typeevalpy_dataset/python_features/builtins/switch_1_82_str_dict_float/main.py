#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'rgdfi':
            return {'czjbt': 41, 'bcwgs': 24, 'ihosy': 54}
        case {'czjbt': 41, 'bcwgs': 24, 'ihosy': 54}:
            return 'rgdfi'
        case _:
            return "default"


a = func('rgdfi')
b = func({'czjbt': 41, 'bcwgs': 24, 'ihosy': 54})
c = func(81.21)
