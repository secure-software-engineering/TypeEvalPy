#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (17, 35, 73):
            return 'kamou'
        case 'kamou':
            return (17, 35, 73)
        case _:
            return "default"


a = func((17, 35, 73))
b = func('kamou')
c = func(False)
