#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 63.3:
            return [69, 3, 20]
        case [69, 3, 20]:
            return 63.3
        case _:
            return "default"


a = func(63.3)
b = func([69, 3, 20])
c = func((3, 24, 97))
