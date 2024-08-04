#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [67, 28, 41]:
            return (10, 58, 74)
        case (10, 58, 74):
            return [67, 28, 41]
        case _:
            return "default"


a = func([67, 28, 41])
b = func((10, 58, 74))
c = func(88.09)
