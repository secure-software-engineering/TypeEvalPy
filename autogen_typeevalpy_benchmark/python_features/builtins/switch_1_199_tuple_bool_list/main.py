#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (26, 92, 78):
            return False
        case False:
            return (26, 92, 78)
        case _:
            return "default"


a = func((26, 92, 78))
b = func(False)
c = func([99, 50, 37])
