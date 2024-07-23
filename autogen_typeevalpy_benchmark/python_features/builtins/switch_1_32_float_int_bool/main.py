#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 41.41:
            return 5
        case 5:
            return 41.41
        case _:
            return "default"


a = func(41.41)
b = func(5)
c = func(False)
