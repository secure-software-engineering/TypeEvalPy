#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [54, 40, 15]:
            return {'wbjxt': 48, 'fhkgf': 39, 'ubcbk': 82}
        case {'wbjxt': 48, 'fhkgf': 39, 'ubcbk': 82}:
            return [54, 40, 15]
        case _:
            return "default"


a = func([54, 40, 15])
b = func({'wbjxt': 48, 'fhkgf': 39, 'ubcbk': 82})
c = func(False)
