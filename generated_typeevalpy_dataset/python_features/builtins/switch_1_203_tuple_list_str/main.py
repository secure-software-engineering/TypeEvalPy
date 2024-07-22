#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (68, 50, 9):
            return [64, 38, 83]
        case [64, 38, 83]:
            return (68, 50, 9)
        case _:
            return "default"


a = func((68, 50, 9))
b = func([64, 38, 83])
c = func('ryrow')
