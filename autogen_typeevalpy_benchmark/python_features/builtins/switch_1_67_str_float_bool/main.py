#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'mbjpi':
            return 74.19
        case 74.19:
            return 'mbjpi'
        case _:
            return "default"


a = func('mbjpi')
b = func(74.19)
c = func(False)
