#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (25, 61, 12):
            return 71
        case 71:
            return (25, 61, 12)
        case _:
            return "default"


a = func((25, 61, 12))
b = func(71)
c = func([60, 43, 84])
