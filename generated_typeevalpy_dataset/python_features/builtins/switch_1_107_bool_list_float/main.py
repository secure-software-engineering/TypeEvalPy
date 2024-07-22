#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return [81, 96, 81]
        case [81, 96, 81]:
            return True
        case _:
            return "default"


a = func(True)
b = func([81, 96, 81])
c = func(16.69)
