#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'ffsft'
        case 'ffsft':
            return True
        case _:
            return "default"


a = func(True)
b = func('ffsft')
c = func((82, 59, 25))
