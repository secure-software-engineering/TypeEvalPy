#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (19, 7, 98):
            return 76.51
        case 76.51:
            return (19, 7, 98)
        case _:
            return "default"


a = func((19, 7, 98))
b = func(76.51)
c = func({'bdcqb': 22, 'iwtsl': 58, 'ccnsj': 32})
