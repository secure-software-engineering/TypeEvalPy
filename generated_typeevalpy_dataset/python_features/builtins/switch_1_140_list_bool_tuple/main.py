#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [5, 9, 56]:
            return True
        case True:
            return [5, 9, 56]
        case _:
            return "default"


a = func([5, 9, 56])
b = func(True)
c = func((77, 83, 34))
