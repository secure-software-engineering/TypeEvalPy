#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 8.04
        case 8.04:
            return True
        case _:
            return "default"


a = func(True)
b = func(8.04)
c = func('cpohx')
