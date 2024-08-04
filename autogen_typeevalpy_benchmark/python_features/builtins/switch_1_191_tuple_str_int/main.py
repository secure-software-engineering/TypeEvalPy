#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (70, 85, 67):
            return 'dbdzy'
        case 'dbdzy':
            return (70, 85, 67)
        case _:
            return "default"


a = func((70, 85, 67))
b = func('dbdzy')
c = func(36)
