#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'gpalu':
            return (7, 56, 2)
        case (7, 56, 2):
            return 'gpalu'
        case _:
            return "default"


a = func('gpalu')
b = func((7, 56, 2))
c = func([50, 73, 69])
