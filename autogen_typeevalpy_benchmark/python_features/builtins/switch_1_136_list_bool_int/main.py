#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [1, 85, 99]:
            return False
        case False:
            return [1, 85, 99]
        case _:
            return "default"


a = func([1, 85, 99])
b = func(False)
c = func(64)
