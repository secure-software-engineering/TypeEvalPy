#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 50.04
        case 50.04:
            return False
        case _:
            return "default"


a = func(False)
b = func(50.04)
c = func(50)
