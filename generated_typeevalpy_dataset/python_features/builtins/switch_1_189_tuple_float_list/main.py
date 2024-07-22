#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (16, 29, 85):
            return 16.93
        case 16.93:
            return (16, 29, 85)
        case _:
            return "default"


a = func((16, 29, 85))
b = func(16.93)
c = func([31, 100, 44])
