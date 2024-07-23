#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'hfbiz': 40, 'wrjnn': 100, 'esfsf': 55}:
            return True
        case True:
            return {'hfbiz': 40, 'wrjnn': 100, 'esfsf': 55}
        case _:
            return "default"


a = func({'hfbiz': 40, 'wrjnn': 100, 'esfsf': 55})
b = func(True)
c = func(50)
