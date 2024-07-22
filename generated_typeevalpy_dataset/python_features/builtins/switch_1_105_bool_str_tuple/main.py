#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 'xpbol'
        case 'xpbol':
            return False
        case _:
            return "default"


a = func(False)
b = func('xpbol')
c = func((20, 82, 27))
