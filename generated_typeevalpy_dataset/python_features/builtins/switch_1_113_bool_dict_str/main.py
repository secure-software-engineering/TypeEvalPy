#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'mnplo': 17, 'mpyfx': 76, 'xndjv': 1}
        case {'mnplo': 17, 'mpyfx': 76, 'xndjv': 1}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'mnplo': 17, 'mpyfx': 76, 'xndjv': 1})
c = func('jusao')
