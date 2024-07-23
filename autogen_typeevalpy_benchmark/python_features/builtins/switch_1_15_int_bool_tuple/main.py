#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 45:
            return False
        case False:
            return 45
        case _:
            return "default"


a = func(45)
b = func(False)
c = func((79, 76, 43))
