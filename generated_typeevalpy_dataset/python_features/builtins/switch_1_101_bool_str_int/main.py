#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 'jqvdm'
        case 'jqvdm':
            return False
        case _:
            return "default"


a = func(False)
b = func('jqvdm')
c = func(73)
