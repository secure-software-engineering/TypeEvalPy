#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (33, 71, 28)
        case (33, 71, 28):
            return False
        case _:
            return "default"


a = func(False)
b = func((33, 71, 28))
c = func('jvbom')
