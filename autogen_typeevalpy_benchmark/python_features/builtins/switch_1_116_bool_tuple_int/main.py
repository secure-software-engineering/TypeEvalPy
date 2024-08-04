#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (98, 85, 42)
        case (98, 85, 42):
            return False
        case _:
            return "default"


a = func(False)
b = func((98, 85, 42))
c = func(6)
