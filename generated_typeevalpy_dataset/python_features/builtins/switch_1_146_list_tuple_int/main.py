#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [65, 96, 67]:
            return (67, 77, 71)
        case (67, 77, 71):
            return [65, 96, 67]
        case _:
            return "default"


a = func([65, 96, 67])
b = func((67, 77, 71))
c = func(20)
