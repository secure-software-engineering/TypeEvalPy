#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [41, 63, 43]:
            return {'tipzq': 90, 'mxygb': 94, 'lddip': 33}
        case {'tipzq': 90, 'mxygb': 94, 'lddip': 33}:
            return [41, 63, 43]
        case _:
            return "default"


a = func([41, 63, 43])
b = func({'tipzq': 90, 'mxygb': 94, 'lddip': 33})
c = func(False)
