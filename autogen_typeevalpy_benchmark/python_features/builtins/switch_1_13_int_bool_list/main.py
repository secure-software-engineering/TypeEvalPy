#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 25:
            return False
        case False:
            return 25
        case _:
            return "default"


a = func(25)
b = func(False)
c = func([76, 90, 48])
