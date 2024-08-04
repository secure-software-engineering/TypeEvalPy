#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return (92, 97, 49)
        case (92, 97, 49):
            return False
        case _:
            return "default"


a = func(False)
b = func((92, 97, 49))
c = func([58, 33, 5])
