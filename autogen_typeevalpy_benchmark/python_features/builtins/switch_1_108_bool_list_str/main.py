#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [16, 6, 2]
        case [16, 6, 2]:
            return False
        case _:
            return "default"


a = func(False)
b = func([16, 6, 2])
c = func('daleg')
