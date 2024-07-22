#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'quxxe':
            return (37, 52, 75)
        case (37, 52, 75):
            return 'quxxe'
        case _:
            return "default"


a = func('quxxe')
b = func((37, 52, 75))
c = func(True)
