#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (81, 93, 44):
            return False
        case False:
            return (81, 93, 44)
        case _:
            return "default"


a = func((81, 93, 44))
b = func(False)
c = func(89.28)
