#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ufddd': 55, 'hlidc': 62, 'moanv': 65}:
            return 5
        case 5:
            return {'ufddd': 55, 'hlidc': 62, 'moanv': 65}
        case _:
            return "default"


a = func({'ufddd': 55, 'hlidc': 62, 'moanv': 65})
b = func(5)
c = func(17.67)
