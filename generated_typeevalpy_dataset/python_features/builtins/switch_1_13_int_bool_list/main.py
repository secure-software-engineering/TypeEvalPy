#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 57:
            return False
        case False:
            return 57
        case _:
            return "default"


a = func(57)
b = func(False)
c = func([29, 81, 77])
