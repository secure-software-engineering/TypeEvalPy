#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 100:
            return 'nmucd'
        case 'nmucd':
            return 100
        case _:
            return "default"


a = func(100)
b = func('nmucd')
c = func([98, 21, 91])
