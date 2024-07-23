#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'jvsvi':
            return 90.1
        case 90.1:
            return 'jvsvi'
        case _:
            return "default"


a = func('jvsvi')
b = func(90.1)
c = func(4)
