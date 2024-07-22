#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (1, 51, 34):
            return 5
        case 5:
            return (1, 51, 34)
        case _:
            return "default"


a = func((1, 51, 34))
b = func(5)
c = func('ldkts')
