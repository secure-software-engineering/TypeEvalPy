#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (34, 85, 25)
        case (34, 85, 25):
            return False
        case _:
            return "default"


a = func(False)
b = func((34, 85, 25))
c = func('ypfoh')
