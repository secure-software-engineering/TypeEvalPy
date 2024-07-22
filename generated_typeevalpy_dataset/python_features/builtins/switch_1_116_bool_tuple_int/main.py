#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (43, 62, 19)
        case (43, 62, 19):
            return False
        case _:
            return "default"


a = func(False)
b = func((43, 62, 19))
c = func(87)
