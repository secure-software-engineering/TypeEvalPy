#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'fvfis':
            return True
        case True:
            return 'fvfis'
        case _:
            return "default"


a = func('fvfis')
b = func(True)
c = func(2.46)
