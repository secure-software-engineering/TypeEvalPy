#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'vlbcw': 14, 'nomlu': 8, 'whaaf': 33}:
            return True
        case True:
            return {'vlbcw': 14, 'nomlu': 8, 'whaaf': 33}
        case _:
            return "default"


a = func({'vlbcw': 14, 'nomlu': 8, 'whaaf': 33})
b = func(True)
c = func((35, 13, 25))
