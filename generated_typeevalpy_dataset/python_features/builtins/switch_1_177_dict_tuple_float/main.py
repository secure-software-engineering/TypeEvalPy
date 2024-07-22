#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'qimxk': 49, 'lobuq': 79, 'utmda': 2}:
            return (7, 47, 12)
        case (7, 47, 12):
            return {'qimxk': 49, 'lobuq': 79, 'utmda': 2}
        case _:
            return "default"


a = func({'qimxk': 49, 'lobuq': 79, 'utmda': 2})
b = func((7, 47, 12))
c = func(78.42)
