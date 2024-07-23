#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [47, 90, 82]:
            return (32, 8, 33)
        case (32, 8, 33):
            return [47, 90, 82]
        case _:
            return "default"


a = func([47, 90, 82])
b = func((32, 8, 33))
c = func({'thwwk': 94, 'pqesg': 58, 'jerrd': 89})
