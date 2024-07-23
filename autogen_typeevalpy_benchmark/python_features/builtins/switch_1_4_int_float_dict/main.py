#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 79:
            return 21.56
        case 21.56:
            return 79
        case _:
            return "default"


a = func(79)
b = func(21.56)
c = func({'orzmi': 23, 'hsazm': 60, 'qvlvr': 72})
