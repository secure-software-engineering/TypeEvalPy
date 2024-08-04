#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [70, 93, 64]:
            return False
        case False:
            return [70, 93, 64]
        case _:
            return "default"


a = func([70, 93, 64])
b = func(False)
c = func(9)
