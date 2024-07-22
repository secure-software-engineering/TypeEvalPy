#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return [89, 70, 6]
        case [89, 70, 6]:
            return True
        case _:
            return "default"


a = func(True)
b = func([89, 70, 6])
c = func(86)
