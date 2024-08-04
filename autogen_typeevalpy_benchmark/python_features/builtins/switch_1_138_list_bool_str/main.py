#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [81, 9, 33]:
            return True
        case True:
            return [81, 9, 33]
        case _:
            return "default"


a = func([81, 9, 33])
b = func(True)
c = func('spnef')
