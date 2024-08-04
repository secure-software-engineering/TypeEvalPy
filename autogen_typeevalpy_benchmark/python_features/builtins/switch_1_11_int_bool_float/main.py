#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 89:
            return False
        case False:
            return 89
        case _:
            return "default"


a = func(89)
b = func(False)
c = func(50.0)
