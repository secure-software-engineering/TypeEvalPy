#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 61:
            return (79, 38, 91)
        case (79, 38, 91):
            return 61
        case _:
            return "default"


a = func(61)
b = func((79, 38, 91))
c = func([47, 89, 68])
