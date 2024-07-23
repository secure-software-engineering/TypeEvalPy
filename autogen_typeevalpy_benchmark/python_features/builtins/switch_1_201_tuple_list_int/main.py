#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (45, 65, 58):
            return [90, 66, 31]
        case [90, 66, 31]:
            return (45, 65, 58)
        case _:
            return "default"


a = func((45, 65, 58))
b = func([90, 66, 31])
c = func(62)
