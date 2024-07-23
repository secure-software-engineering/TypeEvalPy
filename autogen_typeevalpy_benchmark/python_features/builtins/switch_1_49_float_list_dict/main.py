#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 26.35:
            return [30, 46, 64]
        case [30, 46, 64]:
            return 26.35
        case _:
            return "default"


a = func(26.35)
b = func([30, 46, 64])
c = func({'ddraw': 86, 'lcyrn': 74, 'espfu': 62})
