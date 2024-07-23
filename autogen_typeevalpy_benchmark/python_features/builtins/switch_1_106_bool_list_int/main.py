#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [10, 27, 87]
        case [10, 27, 87]:
            return False
        case _:
            return "default"


a = func(False)
b = func([10, 27, 87])
c = func(32)
