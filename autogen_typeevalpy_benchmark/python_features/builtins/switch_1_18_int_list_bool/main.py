#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 90:
            return [10, 22, 57]
        case [10, 22, 57]:
            return 90
        case _:
            return "default"


a = func(90)
b = func([10, 22, 57])
c = func(True)
