#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'zfosf':
            return 22
        case 22:
            return 'zfosf'
        case _:
            return "default"


a = func('zfosf')
b = func(22)
c = func(False)
