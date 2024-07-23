#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 27.61:
            return {'tavaw': 39, 'klzwy': 95, 'gkomf': 65}
        case {'tavaw': 39, 'klzwy': 95, 'gkomf': 65}:
            return 27.61
        case _:
            return "default"


a = func(27.61)
b = func({'tavaw': 39, 'klzwy': 95, 'gkomf': 65})
c = func('iueec')
