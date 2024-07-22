#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 55
        case 55:
            return False
        case _:
            return "default"


a = func(False)
b = func(55)
c = func(42.41)
