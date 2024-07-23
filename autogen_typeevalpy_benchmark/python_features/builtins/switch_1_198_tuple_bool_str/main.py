#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (62, 24, 36):
            return False
        case False:
            return (62, 24, 36)
        case _:
            return "default"


a = func((62, 24, 36))
b = func(False)
c = func('rtzzq')
