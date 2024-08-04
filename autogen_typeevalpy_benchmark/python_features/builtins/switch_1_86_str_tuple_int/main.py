#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'niymb':
            return (64, 92, 86)
        case (64, 92, 86):
            return 'niymb'
        case _:
            return "default"


a = func('niymb')
b = func((64, 92, 86))
c = func(66)
