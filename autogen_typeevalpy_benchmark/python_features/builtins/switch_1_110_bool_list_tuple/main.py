#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return [4, 86, 73]
        case [4, 86, 73]:
            return True
        case _:
            return "default"


a = func(True)
b = func([4, 86, 73])
c = func((47, 7, 61))
