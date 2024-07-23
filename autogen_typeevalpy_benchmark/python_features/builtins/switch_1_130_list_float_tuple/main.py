#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [76, 19, 18]:
            return 34.72
        case 34.72:
            return [76, 19, 18]
        case _:
            return "default"


a = func([76, 19, 18])
b = func(34.72)
c = func((27, 62, 28))
