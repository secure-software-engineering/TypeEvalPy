#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 32.17:
            return 'vvbcc'
        case 'vvbcc':
            return 32.17
        case _:
            return "default"


a = func(32.17)
b = func('vvbcc')
c = func(True)
