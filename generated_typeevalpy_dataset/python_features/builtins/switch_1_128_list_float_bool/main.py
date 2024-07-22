#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [9, 67, 49]:
            return 67.0
        case 67.0:
            return [9, 67, 49]
        case _:
            return "default"


a = func([9, 67, 49])
b = func(67.0)
c = func(False)
