#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 81.98:
            return 61
        case 61:
            return 81.98
        case _:
            return "default"


a = func(81.98)
b = func(61)
c = func({'whnul': 65, 'cfdwf': 29, 'eeeuy': 99})
