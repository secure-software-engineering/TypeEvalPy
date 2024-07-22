#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'msbhq':
            return {'fvkff': 48, 'rvdek': 59, 'krwfv': 37}
        case {'fvkff': 48, 'rvdek': 59, 'krwfv': 37}:
            return 'msbhq'
        case _:
            return "default"


a = func('msbhq')
b = func({'fvkff': 48, 'rvdek': 59, 'krwfv': 37})
c = func((21, 84, 5))
