#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 81.62:
            return 'tsmxh'
        case 'tsmxh':
            return 81.62
        case _:
            return "default"


a = func(81.62)
b = func('tsmxh')
c = func((60, 18, 45))
