#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'eystf': 74, 'rhoqj': 33, 'kwkaf': 86}:
            return (91, 12, 50)
        case (91, 12, 50):
            return {'eystf': 74, 'rhoqj': 33, 'kwkaf': 86}
        case _:
            return "default"


a = func({'eystf': 74, 'rhoqj': 33, 'kwkaf': 86})
b = func((91, 12, 50))
c = func(False)
