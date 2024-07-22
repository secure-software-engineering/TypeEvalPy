#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [72, 44, 17]:
            return False
        case False:
            return [72, 44, 17]
        case _:
            return "default"


a = func([72, 44, 17])
b = func(False)
c = func('bajnn')
