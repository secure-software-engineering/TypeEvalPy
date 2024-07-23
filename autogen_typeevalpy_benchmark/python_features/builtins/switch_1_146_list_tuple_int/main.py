#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [8, 37, 30]:
            return (77, 83, 69)
        case (77, 83, 69):
            return [8, 37, 30]
        case _:
            return "default"


a = func([8, 37, 30])
b = func((77, 83, 69))
c = func(74)
