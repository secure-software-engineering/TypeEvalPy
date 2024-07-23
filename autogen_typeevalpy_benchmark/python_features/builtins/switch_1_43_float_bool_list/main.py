#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 2.9:
            return True
        case True:
            return 2.9
        case _:
            return "default"


a = func(2.9)
b = func(True)
c = func([75, 69, 53])
