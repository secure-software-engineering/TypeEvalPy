#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return [37, 24, 42]
        case [37, 24, 42]:
            return True
        case _:
            return "default"


a = func(True)
b = func([37, 24, 42])
c = func((42, 68, 4))
