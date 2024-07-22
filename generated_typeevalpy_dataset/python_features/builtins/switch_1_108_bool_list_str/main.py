#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [11, 88, 36]
        case [11, 88, 36]:
            return False
        case _:
            return "default"


a = func(False)
b = func([11, 88, 36])
c = func('tzqkb')
