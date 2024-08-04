#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'rjrji':
            return True
        case True:
            return 'rjrji'
        case _:
            return "default"


a = func('rjrji')
b = func(True)
c = func([87, 41, 35])
