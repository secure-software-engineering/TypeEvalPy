#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (35, 51, 23):
            return [95, 53, 16]
        case [95, 53, 16]:
            return (35, 51, 23)
        case _:
            return "default"


a = func((35, 51, 23))
b = func([95, 53, 16])
c = func(True)
