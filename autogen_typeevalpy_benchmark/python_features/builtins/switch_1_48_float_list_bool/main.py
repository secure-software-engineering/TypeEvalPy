#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 73.48:
            return [12, 93, 100]
        case [12, 93, 100]:
            return 73.48
        case _:
            return "default"


a = func(73.48)
b = func([12, 93, 100])
c = func(True)
