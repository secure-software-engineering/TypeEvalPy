#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (71, 7, 95):
            return False
        case False:
            return (71, 7, 95)
        case _:
            return "default"


a = func((71, 7, 95))
b = func(False)
c = func(45.52)
