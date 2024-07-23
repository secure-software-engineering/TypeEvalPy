#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 53.4:
            return False
        case False:
            return 53.4
        case _:
            return "default"


a = func(53.4)
b = func(False)
c = func('bvztn')
