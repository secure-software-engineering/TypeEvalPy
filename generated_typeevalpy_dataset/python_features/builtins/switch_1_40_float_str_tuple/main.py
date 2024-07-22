#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 19.23:
            return 'jwkit'
        case 'jwkit':
            return 19.23
        case _:
            return "default"


a = func(19.23)
b = func('jwkit')
c = func((33, 100, 1))
