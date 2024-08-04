#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 28.37:
            return False
        case False:
            return 28.37
        case _:
            return "default"


a = func(28.37)
b = func(False)
c = func(45)
