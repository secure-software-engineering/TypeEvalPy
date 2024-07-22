#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'frbkw':
            return False
        case False:
            return 'frbkw'
        case _:
            return "default"


a = func('frbkw')
b = func(False)
c = func([11, 9, 98])
