#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return [38, 50, 35]
        case [38, 50, 35]:
            return True
        case _:
            return "default"


a = func(True)
b = func([38, 50, 35])
c = func(49.11)
