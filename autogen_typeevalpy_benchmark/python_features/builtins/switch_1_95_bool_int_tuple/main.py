#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 32
        case 32:
            return False
        case _:
            return "default"


a = func(False)
b = func(32)
c = func((87, 82, 77))
