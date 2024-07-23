#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 44.09:
            return False
        case False:
            return 44.09
        case _:
            return "default"


a = func(44.09)
b = func(False)
c = func(84)
