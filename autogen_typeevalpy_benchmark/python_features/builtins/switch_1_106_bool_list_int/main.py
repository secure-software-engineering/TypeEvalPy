#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return [92, 57, 67]
        case [92, 57, 67]:
            return True
        case _:
            return "default"


a = func(True)
b = func([92, 57, 67])
c = func(28)
