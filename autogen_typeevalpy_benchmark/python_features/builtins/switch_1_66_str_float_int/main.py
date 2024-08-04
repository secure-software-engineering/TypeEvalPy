#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'nopqu':
            return 5.13
        case 5.13:
            return 'nopqu'
        case _:
            return "default"


a = func('nopqu')
b = func(5.13)
c = func(65)
