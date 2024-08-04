#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (24, 28, 25):
            return [47, 59, 5]
        case [47, 59, 5]:
            return (24, 28, 25)
        case _:
            return "default"


a = func((24, 28, 25))
b = func([47, 59, 5])
c = func({'hgjst': 73, 'wyfwy': 43, 'ccixg': 62})
