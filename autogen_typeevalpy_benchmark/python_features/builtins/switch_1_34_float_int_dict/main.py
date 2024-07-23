#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 3.82:
            return 61
        case 61:
            return 3.82
        case _:
            return "default"


a = func(3.82)
b = func(61)
c = func({'xqwwb': 93, 'zrvga': 99, 'ccilz': 76})
