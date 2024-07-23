#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 14.64:
            return 'pfzow'
        case 'pfzow':
            return 14.64
        case _:
            return "default"


a = func(14.64)
b = func('pfzow')
c = func([5, 67, 64])
