#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 63.31:
            return 'zptor'
        case 'zptor':
            return 63.31
        case _:
            return "default"


a = func(63.31)
b = func('zptor')
c = func(False)
