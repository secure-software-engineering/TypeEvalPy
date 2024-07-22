#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 4.19:
            return [91, 78, 84]
        case [91, 78, 84]:
            return 4.19
        case _:
            return "default"


a = func(4.19)
b = func([91, 78, 84])
c = func(True)
