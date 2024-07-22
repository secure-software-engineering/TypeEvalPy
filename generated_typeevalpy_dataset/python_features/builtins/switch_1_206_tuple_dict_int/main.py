#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (93, 39, 69):
            return {'ajnfb': 8, 'atitb': 59, 'hdkqs': 24}
        case {'ajnfb': 8, 'atitb': 59, 'hdkqs': 24}:
            return (93, 39, 69)
        case _:
            return "default"


a = func((93, 39, 69))
b = func({'ajnfb': 8, 'atitb': 59, 'hdkqs': 24})
c = func(56)
