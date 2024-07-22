#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 30.18:
            return (64, 17, 43)
        case (64, 17, 43):
            return 30.18
        case _:
            return "default"


a = func(30.18)
b = func((64, 17, 43))
c = func(True)
