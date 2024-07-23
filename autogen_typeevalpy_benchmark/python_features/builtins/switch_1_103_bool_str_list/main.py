#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'majns'
        case 'majns':
            return True
        case _:
            return "default"


a = func(True)
b = func('majns')
c = func([68, 100, 55])
