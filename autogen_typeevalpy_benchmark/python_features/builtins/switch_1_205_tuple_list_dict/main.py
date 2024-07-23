#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (59, 25, 58):
            return [30, 24, 18]
        case [30, 24, 18]:
            return (59, 25, 58)
        case _:
            return "default"


a = func((59, 25, 58))
b = func([30, 24, 18])
c = func({'yzzii': 94, 'mdmje': 95, 'msbef': 77})
