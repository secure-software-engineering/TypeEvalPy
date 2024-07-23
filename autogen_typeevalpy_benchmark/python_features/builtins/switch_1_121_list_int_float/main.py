#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [7, 48, 8]:
            return 42
        case 42:
            return [7, 48, 8]
        case _:
            return "default"


a = func([7, 48, 8])
b = func(42)
c = func(20.3)
