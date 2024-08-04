#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 97:
            return 13.3
        case 13.3:
            return 97
        case _:
            return "default"


a = func(97)
b = func(13.3)
c = func('juvpb')
