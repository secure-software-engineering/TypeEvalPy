#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 11:
            return {'vcbrx': 5, 'caeqp': 54, 'gjtki': 95}
        case {'vcbrx': 5, 'caeqp': 54, 'gjtki': 95}:
            return 11
        case _:
            return "default"


a = func(11)
b = func({'vcbrx': 5, 'caeqp': 54, 'gjtki': 95})
c = func(87.63)
