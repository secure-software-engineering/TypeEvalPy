#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [42, 5, 95]:
            return True
        case True:
            return [42, 5, 95]
        case _:
            return "default"


a = func([42, 5, 95])
b = func(True)
c = func(33.43)
