#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'crxvv':
            return (47, 34, 38)
        case (47, 34, 38):
            return 'crxvv'
        case _:
            return "default"


a = func('crxvv')
b = func((47, 34, 38))
c = func(91.29)
