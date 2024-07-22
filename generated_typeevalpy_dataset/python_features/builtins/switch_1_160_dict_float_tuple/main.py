#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'chnih': 62, 'notfv': 10, 'gmuqp': 96}:
            return 11.67
        case 11.67:
            return {'chnih': 62, 'notfv': 10, 'gmuqp': 96}
        case _:
            return "default"


a = func({'chnih': 62, 'notfv': 10, 'gmuqp': 96})
b = func(11.67)
c = func((21, 42, 83))
