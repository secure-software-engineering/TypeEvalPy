#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [84, 8, 18]
        case [84, 8, 18]:
            return False
        case _:
            return "default"


a = func(False)
b = func([84, 8, 18])
c = func((47, 83, 20))
