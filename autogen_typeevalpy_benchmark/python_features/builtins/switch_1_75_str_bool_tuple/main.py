#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'ahtqm':
            return True
        case True:
            return 'ahtqm'
        case _:
            return "default"


a = func('ahtqm')
b = func(True)
c = func((16, 23, 38))
