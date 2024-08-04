#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 31.9:
            return 35
        case 35:
            return 31.9
        case _:
            return "default"


a = func(31.9)
b = func(35)
c = func('sozze')
