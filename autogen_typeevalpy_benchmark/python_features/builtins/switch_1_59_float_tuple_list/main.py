#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 3.35:
            return (12, 58, 6)
        case (12, 58, 6):
            return 3.35
        case _:
            return "default"


a = func(3.35)
b = func((12, 58, 6))
c = func([18, 67, 34])
