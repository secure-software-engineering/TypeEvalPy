#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'kdgll': 52, 'qpipx': 59, 'myrrt': 88}:
            return True
        case True:
            return {'kdgll': 52, 'qpipx': 59, 'myrrt': 88}
        case _:
            return "default"


a = func({'kdgll': 52, 'qpipx': 59, 'myrrt': 88})
b = func(True)
c = func(5.98)
