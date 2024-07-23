#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return [21, 64, 48]
        case [21, 64, 48]:
            return False
        case _:
            return "default"


a = func(False)
b = func([21, 64, 48])
c = func('tmzxc')
