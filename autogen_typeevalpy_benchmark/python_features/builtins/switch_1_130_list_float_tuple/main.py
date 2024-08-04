#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [53, 84, 78]:
            return 5.57
        case 5.57:
            return [53, 84, 78]
        case _:
            return "default"


a = func([53, 84, 78])
b = func(5.57)
c = func((27, 4, 26))
