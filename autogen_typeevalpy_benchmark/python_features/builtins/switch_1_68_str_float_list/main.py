#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'yvctl':
            return 72.69
        case 72.69:
            return 'yvctl'
        case _:
            return "default"


a = func('yvctl')
b = func(72.69)
c = func([36, 15, 69])
