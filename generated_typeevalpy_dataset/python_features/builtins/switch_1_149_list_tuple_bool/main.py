#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [67, 31, 38]:
            return (44, 73, 84)
        case (44, 73, 84):
            return [67, 31, 38]
        case _:
            return "default"


a = func([67, 31, 38])
b = func((44, 73, 84))
c = func(False)
