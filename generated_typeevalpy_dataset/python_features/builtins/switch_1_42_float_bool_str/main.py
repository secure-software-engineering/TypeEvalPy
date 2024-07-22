#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 77.14:
            return False
        case False:
            return 77.14
        case _:
            return "default"


a = func(77.14)
b = func(False)
c = func('fnvch')
