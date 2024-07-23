#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'tldhv'
        case 'tldhv':
            return True
        case _:
            return "default"


a = func(True)
b = func('tldhv')
c = func((94, 19, 94))
