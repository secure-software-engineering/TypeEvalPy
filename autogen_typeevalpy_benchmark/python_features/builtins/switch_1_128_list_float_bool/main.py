#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [62, 24, 10]:
            return 16.28
        case 16.28:
            return [62, 24, 10]
        case _:
            return "default"


a = func([62, 24, 10])
b = func(16.28)
c = func(True)
