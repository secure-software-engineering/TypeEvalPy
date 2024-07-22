#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 86.62:
            return False
        case False:
            return 86.62
        case _:
            return "default"


a = func(86.62)
b = func(False)
c = func((44, 77, 47))
