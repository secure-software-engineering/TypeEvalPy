#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'mxhar'
        case 'mxhar':
            return True
        case _:
            return "default"


a = func(True)
b = func('mxhar')
c = func(97.87)
