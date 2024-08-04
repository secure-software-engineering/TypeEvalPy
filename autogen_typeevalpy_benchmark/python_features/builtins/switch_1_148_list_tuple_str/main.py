#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [26, 84, 65]:
            return (59, 92, 12)
        case (59, 92, 12):
            return [26, 84, 65]
        case _:
            return "default"


a = func([26, 84, 65])
b = func((59, 92, 12))
c = func('rizyx')
