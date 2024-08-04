#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [99, 96, 75]
        case [99, 96, 75]:
            return False
        case _:
            return "default"


a = func(False)
b = func([99, 96, 75])
c = func(19.52)
