#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [57, 59, 99]:
            return 42.64
        case 42.64:
            return [57, 59, 99]
        case _:
            return "default"


a = func([57, 59, 99])
b = func(42.64)
c = func({'idogf': 90, 'lymvz': 49, 'bwekv': 12})
