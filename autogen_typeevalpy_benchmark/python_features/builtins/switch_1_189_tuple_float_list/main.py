#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (61, 10, 93):
            return 9.78
        case 9.78:
            return (61, 10, 93)
        case _:
            return "default"


a = func((61, 10, 93))
b = func(9.78)
c = func([7, 86, 51])
