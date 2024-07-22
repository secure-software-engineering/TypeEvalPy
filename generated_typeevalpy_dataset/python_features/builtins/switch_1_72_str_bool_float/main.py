#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'tgxcm':
            return True
        case True:
            return 'tgxcm'
        case _:
            return "default"


a = func('tgxcm')
b = func(True)
c = func(51.67)
