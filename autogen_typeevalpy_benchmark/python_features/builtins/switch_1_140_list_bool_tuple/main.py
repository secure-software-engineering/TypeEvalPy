#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [56, 96, 10]:
            return True
        case True:
            return [56, 96, 10]
        case _:
            return "default"


a = func([56, 96, 10])
b = func(True)
c = func((82, 77, 47))
