#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 16.09:
            return (67, 24, 59)
        case (67, 24, 59):
            return 16.09
        case _:
            return "default"


a = func(16.09)
b = func((67, 24, 59))
c = func(76)
