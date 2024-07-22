#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 69.42:
            return {'omcmp': 14, 'kqono': 41, 'zvguv': 56}
        case {'omcmp': 14, 'kqono': 41, 'zvguv': 56}:
            return 69.42
        case _:
            return "default"


a = func(69.42)
b = func({'omcmp': 14, 'kqono': 41, 'zvguv': 56})
c = func(14)
