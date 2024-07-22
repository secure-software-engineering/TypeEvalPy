#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'wcvrk': 91, 'guyll': 86, 'czucg': 86}:
            return True
        case True:
            return {'wcvrk': 91, 'guyll': 86, 'czucg': 86}
        case _:
            return "default"


a = func({'wcvrk': 91, 'guyll': 86, 'czucg': 86})
b = func(True)
c = func([99, 45, 98])
