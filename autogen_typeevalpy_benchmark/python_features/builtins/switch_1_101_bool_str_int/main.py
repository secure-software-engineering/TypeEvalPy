#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'qannl'
        case 'qannl':
            return True
        case _:
            return "default"


a = func(True)
b = func('qannl')
c = func(65)
