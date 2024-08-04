#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'tzbjl':
            return False
        case False:
            return 'tzbjl'
        case _:
            return "default"


a = func('tzbjl')
b = func(False)
c = func(19.41)
