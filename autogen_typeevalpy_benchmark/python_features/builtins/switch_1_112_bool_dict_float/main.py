#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return {'sphxo': 80, 'elgls': 81, 'niskj': 49}
        case {'sphxo': 80, 'elgls': 81, 'niskj': 49}:
            return True
        case _:
            return "default"


a = func(True)
b = func({'sphxo': 80, 'elgls': 81, 'niskj': 49})
c = func(62.74)
