#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 'wthqg'
        case 'wthqg':
            return False
        case _:
            return "default"


a = func(False)
b = func('wthqg')
c = func(23.99)
