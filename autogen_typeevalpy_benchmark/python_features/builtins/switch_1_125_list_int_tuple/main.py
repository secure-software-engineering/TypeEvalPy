#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [75, 23, 56]:
            return 90
        case 90:
            return [75, 23, 56]
        case _:
            return "default"


a = func([75, 23, 56])
b = func(90)
c = func((76, 18, 97))
