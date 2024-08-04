#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 57.42
        case 57.42:
            return False
        case _:
            return "default"


a = func(False)
b = func(57.42)
c = func([93, 34, 44])
