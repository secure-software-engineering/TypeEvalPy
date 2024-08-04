#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 70.9:
            return 'xsxhz'
        case 'xsxhz':
            return 70.9
        case _:
            return "default"


a = func(70.9)
b = func('xsxhz')
c = func({'sxmwb': 3, 'liuvb': 89, 'gfauw': 87})
