#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 56.12
        case 56.12:
            return False
        case _:
            return "default"


a = func(False)
b = func(56.12)
c = func('jrgcw')
