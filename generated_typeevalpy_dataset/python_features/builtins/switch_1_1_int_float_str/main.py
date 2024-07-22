#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 78:
            return 13.77
        case 13.77:
            return 78
        case _:
            return "default"


a = func(78)
b = func(13.77)
c = func('gvfrk')
