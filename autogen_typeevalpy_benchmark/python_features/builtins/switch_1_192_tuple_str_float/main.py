#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (69, 23, 9):
            return 'pttni'
        case 'pttni':
            return (69, 23, 9)
        case _:
            return "default"


a = func((69, 23, 9))
b = func('pttni')
c = func(75.35)
