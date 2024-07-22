#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [69, 100, 66]:
            return (33, 22, 41)
        case (33, 22, 41):
            return [69, 100, 66]
        case _:
            return "default"


a = func([69, 100, 66])
b = func((33, 22, 41))
c = func(29.9)
