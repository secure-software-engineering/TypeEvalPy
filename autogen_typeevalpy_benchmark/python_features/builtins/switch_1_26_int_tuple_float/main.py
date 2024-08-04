#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 11:
            return (28, 66, 47)
        case (28, 66, 47):
            return 11
        case _:
            return "default"


a = func(11)
b = func((28, 66, 47))
c = func(69.64)
