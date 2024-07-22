#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 19:
            return (63, 92, 30)
        case (63, 92, 30):
            return 19
        case _:
            return "default"


a = func(19)
b = func((63, 92, 30))
c = func(True)
