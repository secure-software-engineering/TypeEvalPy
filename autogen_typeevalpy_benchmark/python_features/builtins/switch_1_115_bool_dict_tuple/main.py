#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return {'osmvx': 4, 'yumnk': 92, 'fbnpq': 62}
        case {'osmvx': 4, 'yumnk': 92, 'fbnpq': 62}:
            return False
        case _:
            return "default"


a = func(False)
b = func({'osmvx': 4, 'yumnk': 92, 'fbnpq': 62})
c = func((88, 67, 87))
