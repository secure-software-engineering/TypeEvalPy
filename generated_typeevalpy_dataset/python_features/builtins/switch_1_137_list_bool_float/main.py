#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [97, 10, 76]:
            return False
        case False:
            return [97, 10, 76]
        case _:
            return "default"


a = func([97, 10, 76])
b = func(False)
c = func(25.77)
