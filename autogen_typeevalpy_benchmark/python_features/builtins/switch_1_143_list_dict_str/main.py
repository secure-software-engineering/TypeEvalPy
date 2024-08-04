#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [56, 40, 43]:
            return {'wybjh': 56, 'qnnpn': 10, 'zmhhe': 88}
        case {'wybjh': 56, 'qnnpn': 10, 'zmhhe': 88}:
            return [56, 40, 43]
        case _:
            return "default"


a = func([56, 40, 43])
b = func({'wybjh': 56, 'qnnpn': 10, 'zmhhe': 88})
c = func('sjbxe')
