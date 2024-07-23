#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'lcmni':
            return 81
        case 81:
            return 'lcmni'
        case _:
            return "default"


a = func('lcmni')
b = func(81)
c = func([13, 42, 95])
