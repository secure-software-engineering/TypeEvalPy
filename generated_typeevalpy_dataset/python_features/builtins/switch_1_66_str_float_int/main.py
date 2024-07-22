#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'phcaq':
            return 61.3
        case 61.3:
            return 'phcaq'
        case _:
            return "default"


a = func('phcaq')
b = func(61.3)
c = func(4)
