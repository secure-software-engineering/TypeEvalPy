#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 79:
            return [80, 83, 15]
        case [80, 83, 15]:
            return 79
        case _:
            return "default"


a = func(79)
b = func([80, 83, 15])
c = func({'fewqg': 39, 'lyfhn': 59, 'qcimw': 48})
