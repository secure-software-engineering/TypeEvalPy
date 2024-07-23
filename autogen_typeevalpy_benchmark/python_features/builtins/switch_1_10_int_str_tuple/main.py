#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 48:
            return 'lwcdb'
        case 'lwcdb':
            return 48
        case _:
            return "default"


a = func(48)
b = func('lwcdb')
c = func((77, 3, 7))
