#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (36, 84, 6):
            return 2
        case 2:
            return (36, 84, 6)
        case _:
            return "default"


a = func((36, 84, 6))
b = func(2)
c = func(81.41)
