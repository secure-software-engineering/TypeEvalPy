#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (44, 56, 10):
            return [67, 93, 4]
        case [67, 93, 4]:
            return (44, 56, 10)
        case _:
            return "default"


a = func((44, 56, 10))
b = func([67, 93, 4])
c = func(76.8)
