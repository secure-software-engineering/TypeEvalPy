#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 93
        case 93:
            return False
        case _:
            return "default"


a = func(False)
b = func(93)
c = func('uvhvy')
