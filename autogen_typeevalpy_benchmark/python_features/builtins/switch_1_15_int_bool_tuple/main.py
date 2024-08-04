#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 35:
            return False
        case False:
            return 35
        case _:
            return "default"


a = func(35)
b = func(False)
c = func((14, 8, 92))
