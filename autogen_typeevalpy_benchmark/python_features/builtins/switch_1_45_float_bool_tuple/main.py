#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 63.6:
            return False
        case False:
            return 63.6
        case _:
            return "default"


a = func(63.6)
b = func(False)
c = func((44, 32, 42))
