#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return (46, 53, 7)
        case (46, 53, 7):
            return True
        case _:
            return "default"


a = func(True)
b = func((46, 53, 7))
c = func({'lmifi': 72, 'djtjf': 23, 'eswtz': 35})
