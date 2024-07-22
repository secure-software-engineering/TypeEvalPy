#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 42:
            return (60, 5, 6)
        case (60, 5, 6):
            return 42
        case _:
            return "default"


a = func(42)
b = func((60, 5, 6))
c = func('vpngq')
