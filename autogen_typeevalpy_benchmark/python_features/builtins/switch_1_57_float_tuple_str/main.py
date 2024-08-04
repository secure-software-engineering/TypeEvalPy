#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 25.1:
            return (54, 39, 71)
        case (54, 39, 71):
            return 25.1
        case _:
            return "default"


a = func(25.1)
b = func((54, 39, 71))
c = func('ysrxd')
