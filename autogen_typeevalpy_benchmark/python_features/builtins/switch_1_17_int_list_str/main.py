#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 100:
            return [96, 76, 61]
        case [96, 76, 61]:
            return 100
        case _:
            return "default"


a = func(100)
b = func([96, 76, 61])
c = func('gfhpc')
