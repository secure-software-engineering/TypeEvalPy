#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 18.61:
            return False
        case False:
            return 18.61
        case _:
            return "default"


a = func(18.61)
b = func(False)
c = func([97, 93, 97])
