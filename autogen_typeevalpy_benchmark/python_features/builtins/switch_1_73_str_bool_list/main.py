#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'sjgxz':
            return True
        case True:
            return 'sjgxz'
        case _:
            return "default"


a = func('sjgxz')
b = func(True)
c = func([95, 68, 46])
