#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 9.03
        case 9.03:
            return True
        case _:
            return "default"


a = func(True)
b = func(9.03)
c = func('esiwg')
