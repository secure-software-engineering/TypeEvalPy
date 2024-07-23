#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ilsnm': 10, 'pmkgo': 97, 'ddkwv': 72}:
            return (23, 77, 97)
        case (23, 77, 97):
            return {'ilsnm': 10, 'pmkgo': 97, 'ddkwv': 72}
        case _:
            return "default"


a = func({'ilsnm': 10, 'pmkgo': 97, 'ddkwv': 72})
b = func((23, 77, 97))
c = func(True)
