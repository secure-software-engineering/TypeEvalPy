#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (69, 4, 10):
            return 88.69
        case 88.69:
            return (69, 4, 10)
        case _:
            return "default"


a = func((69, 4, 10))
b = func(88.69)
c = func('pjebi')
