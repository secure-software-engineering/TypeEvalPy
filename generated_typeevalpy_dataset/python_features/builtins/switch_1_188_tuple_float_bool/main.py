#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (86, 84, 68):
            return 30.23
        case 30.23:
            return (86, 84, 68)
        case _:
            return "default"


a = func((86, 84, 68))
b = func(30.23)
c = func(False)
