#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [4, 89, 72]:
            return False
        case False:
            return [4, 89, 72]
        case _:
            return "default"


a = func([4, 89, 72])
b = func(False)
c = func(67)
