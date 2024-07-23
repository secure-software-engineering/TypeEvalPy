#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [75, 9, 10]:
            return 19
        case 19:
            return [75, 9, 10]
        case _:
            return "default"


a = func([75, 9, 10])
b = func(19)
c = func((34, 31, 18))
