#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 29.64:
            return True
        case True:
            return 29.64
        case _:
            return "default"


a = func(29.64)
b = func(True)
c = func('lvzpf')
