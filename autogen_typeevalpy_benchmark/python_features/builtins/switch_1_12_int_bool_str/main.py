#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 5:
            return True
        case True:
            return 5
        case _:
            return "default"


a = func(5)
b = func(True)
c = func('xlbha')
