#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 97.28:
            return (9, 55, 82)
        case (9, 55, 82):
            return 97.28
        case _:
            return "default"


a = func(97.28)
b = func((9, 55, 82))
c = func({'onqqe': 64, 'booww': 33, 'fdaei': 28})
