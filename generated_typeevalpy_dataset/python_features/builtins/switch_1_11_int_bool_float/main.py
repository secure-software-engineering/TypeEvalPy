#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 52:
            return False
        case False:
            return 52
        case _:
            return "default"


a = func(52)
b = func(False)
c = func(78.13)
