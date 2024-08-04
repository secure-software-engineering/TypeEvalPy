#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'yfikl':
            return True
        case True:
            return 'yfikl'
        case _:
            return "default"


a = func('yfikl')
b = func(True)
c = func(7)
