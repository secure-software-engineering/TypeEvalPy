#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [1, 38, 92]:
            return False
        case False:
            return [1, 38, 92]
        case _:
            return "default"


a = func([1, 38, 92])
b = func(False)
c = func((66, 34, 100))
