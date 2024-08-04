#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (85, 38, 6):
            return 44
        case 44:
            return (85, 38, 6)
        case _:
            return "default"


a = func((85, 38, 6))
b = func(44)
c = func([66, 30, 42])
