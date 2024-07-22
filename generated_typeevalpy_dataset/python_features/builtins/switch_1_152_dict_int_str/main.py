#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'uhlxn': 75, 'wgecl': 14, 'jxqqg': 45}:
            return 18
        case 18:
            return {'uhlxn': 75, 'wgecl': 14, 'jxqqg': 45}
        case _:
            return "default"


a = func({'uhlxn': 75, 'wgecl': 14, 'jxqqg': 45})
b = func(18)
c = func('jerlo')
