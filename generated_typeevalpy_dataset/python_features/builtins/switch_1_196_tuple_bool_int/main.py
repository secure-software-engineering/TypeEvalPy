#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (47, 32, 84):
            return False
        case False:
            return (47, 32, 84)
        case _:
            return "default"


a = func((47, 32, 84))
b = func(False)
c = func(5)
