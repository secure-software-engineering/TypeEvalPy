#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (100, 74, 30):
            return {'pjwhl': 90, 'rixmp': 16, 'henya': 87}
        case {'pjwhl': 90, 'rixmp': 16, 'henya': 87}:
            return (100, 74, 30)
        case _:
            return "default"


a = func((100, 74, 30))
b = func({'pjwhl': 90, 'rixmp': 16, 'henya': 87})
c = func(True)
