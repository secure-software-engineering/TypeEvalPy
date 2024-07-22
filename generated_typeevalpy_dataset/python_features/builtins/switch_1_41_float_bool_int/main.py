#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 10.62:
            return False
        case False:
            return 10.62
        case _:
            return "default"


a = func(10.62)
b = func(False)
c = func(88)
