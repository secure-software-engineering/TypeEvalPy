#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (69, 37, 35):
            return True
        case True:
            return (69, 37, 35)
        case _:
            return "default"


a = func((69, 37, 35))
b = func(True)
c = func({'rgoit': 32, 'ujspo': 43, 'orkue': 29})
