#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (43, 11, 84):
            return 'qlyly'
        case 'qlyly':
            return (43, 11, 84)
        case _:
            return "default"


a = func((43, 11, 84))
b = func('qlyly')
c = func(45.45)
