#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'ssosa':
            return 35.1
        case 35.1:
            return 'ssosa'
        case _:
            return "default"


a = func('ssosa')
b = func(35.1)
c = func([59, 97, 31])
