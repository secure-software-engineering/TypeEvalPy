#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 31.68:
            return False
        case False:
            return 31.68
        case _:
            return "default"


a = func(31.68)
b = func(False)
c = func([61, 62, 83])
