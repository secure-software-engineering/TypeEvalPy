#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'mvpam': 58, 'lgrnf': 3, 'varpd': 67}:
            return 'qblbz'
        case 'qblbz':
            return {'mvpam': 58, 'lgrnf': 3, 'varpd': 67}
        case _:
            return "default"


a = func({'mvpam': 58, 'lgrnf': 3, 'varpd': 67})
b = func('qblbz')
c = func(64)
