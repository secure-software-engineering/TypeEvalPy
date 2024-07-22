#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'zimwt':
            return False
        case False:
            return 'zimwt'
        case _:
            return "default"


a = func('zimwt')
b = func(False)
c = func((29, 73, 64))
