#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 52:
            return True
        case True:
            return 52
        case _:
            return "default"


a = func(52)
b = func(True)
c = func('tfjwj')
