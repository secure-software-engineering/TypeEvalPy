#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'jhsmm':
            return (37, 100, 36)
        case (37, 100, 36):
            return 'jhsmm'
        case _:
            return "default"


a = func('jhsmm')
b = func((37, 100, 36))
c = func(False)
