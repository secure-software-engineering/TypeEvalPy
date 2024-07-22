#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [46, 25, 34]:
            return 100
        case 100:
            return [46, 25, 34]
        case _:
            return "default"


a = func([46, 25, 34])
b = func(100)
c = func('crtjz')
