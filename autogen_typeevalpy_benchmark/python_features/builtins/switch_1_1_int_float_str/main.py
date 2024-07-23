#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 62:
            return 26.89
        case 26.89:
            return 62
        case _:
            return "default"


a = func(62)
b = func(26.89)
c = func('nxygy')
