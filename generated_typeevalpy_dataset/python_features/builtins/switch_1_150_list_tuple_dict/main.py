#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [44, 11, 10]:
            return (99, 28, 34)
        case (99, 28, 34):
            return [44, 11, 10]
        case _:
            return "default"


a = func([44, 11, 10])
b = func((99, 28, 34))
c = func({'qyasz': 40, 'vqgsm': 80, 'uowdj': 40})
