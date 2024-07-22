#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (2, 1, 23):
            return 'dhmvc'
        case 'dhmvc':
            return (2, 1, 23)
        case _:
            return "default"


a = func((2, 1, 23))
b = func('dhmvc')
c = func([23, 76, 64])
