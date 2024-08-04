#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (52, 19, 14)
        case (52, 19, 14):
            return False
        case _:
            return "default"


a = func(False)
b = func((52, 19, 14))
c = func(49.21)
