#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 94.83
        case 94.83:
            return False
        case _:
            return "default"


a = func(False)
b = func(94.83)
c = func(20)
