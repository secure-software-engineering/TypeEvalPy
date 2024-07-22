#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 64:
            return False
        case False:
            return 64
        case _:
            return "default"


a = func(64)
b = func(False)
c = func('lbuzp')
