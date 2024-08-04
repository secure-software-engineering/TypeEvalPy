#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (55, 40, 43):
            return 'bxwmu'
        case 'bxwmu':
            return (55, 40, 43)
        case _:
            return "default"


a = func((55, 40, 43))
b = func('bxwmu')
c = func([17, 20, 86])
