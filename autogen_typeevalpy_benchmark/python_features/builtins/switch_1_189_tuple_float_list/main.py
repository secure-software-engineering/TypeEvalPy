#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (67, 49, 95):
            return 29.67
        case 29.67:
            return (67, 49, 95)
        case _:
            return "default"


a = func((67, 49, 95))
b = func(29.67)
c = func([32, 63, 5])
