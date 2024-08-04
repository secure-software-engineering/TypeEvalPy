#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 38:
            return 'tdfzu'
        case 'tdfzu':
            return 38
        case _:
            return "default"


a = func(38)
b = func('tdfzu')
c = func([18, 75, 29])
