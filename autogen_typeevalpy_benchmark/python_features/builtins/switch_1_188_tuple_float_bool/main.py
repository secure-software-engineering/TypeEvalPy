#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (36, 81, 87):
            return 79.77
        case 79.77:
            return (36, 81, 87)
        case _:
            return "default"


a = func((36, 81, 87))
b = func(79.77)
c = func(False)
