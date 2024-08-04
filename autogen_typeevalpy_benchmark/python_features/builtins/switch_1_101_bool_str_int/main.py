#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'fzkrd'
        case 'fzkrd':
            return True
        case _:
            return "default"


a = func(True)
b = func('fzkrd')
c = func(50)
