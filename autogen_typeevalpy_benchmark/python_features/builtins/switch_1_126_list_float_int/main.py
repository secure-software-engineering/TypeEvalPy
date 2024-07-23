#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [38, 74, 55]:
            return 44.47
        case 44.47:
            return [38, 74, 55]
        case _:
            return "default"


a = func([38, 74, 55])
b = func(44.47)
c = func(5)
