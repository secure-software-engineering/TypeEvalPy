#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [31, 32, 57]:
            return 'abhps'
        case 'abhps':
            return [31, 32, 57]
        case _:
            return "default"


a = func([31, 32, 57])
b = func('abhps')
c = func({'rzxhk': 62, 'lrqwj': 91, 'nslwx': 63})
