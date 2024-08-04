#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (22, 80, 78):
            return True
        case True:
            return (22, 80, 78)
        case _:
            return "default"


a = func((22, 80, 78))
b = func(True)
c = func(28)
