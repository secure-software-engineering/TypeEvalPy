#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 51:
            return (74, 75, 25)
        case (74, 75, 25):
            return 51
        case _:
            return "default"


a = func(51)
b = func((74, 75, 25))
c = func('pheia')
