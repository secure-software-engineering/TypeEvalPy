#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (43, 90, 53):
            return 'msmkb'
        case 'msmkb':
            return (43, 90, 53)
        case _:
            return "default"


a = func((43, 90, 53))
b = func('msmkb')
c = func(86.19)
