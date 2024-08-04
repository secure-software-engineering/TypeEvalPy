#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [56, 32, 85]:
            return (27, 70, 92)
        case (27, 70, 92):
            return [56, 32, 85]
        case _:
            return "default"


a = func([56, 32, 85])
b = func((27, 70, 92))
c = func(False)
