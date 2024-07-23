#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [14, 92, 40]:
            return False
        case False:
            return [14, 92, 40]
        case _:
            return "default"


a = func([14, 92, 40])
b = func(False)
c = func('agazl')
