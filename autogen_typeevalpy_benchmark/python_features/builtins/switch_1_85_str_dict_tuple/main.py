#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'rzvim':
            return {'ichiu': 18, 'szpxf': 30, 'pasyn': 10}
        case {'ichiu': 18, 'szpxf': 30, 'pasyn': 10}:
            return 'rzvim'
        case _:
            return "default"


a = func('rzvim')
b = func({'ichiu': 18, 'szpxf': 30, 'pasyn': 10})
c = func((21, 30, 100))
