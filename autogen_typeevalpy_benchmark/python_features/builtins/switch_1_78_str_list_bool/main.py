#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'pfjkh':
            return [27, 77, 53]
        case [27, 77, 53]:
            return 'pfjkh'
        case _:
            return "default"


a = func('pfjkh')
b = func([27, 77, 53])
c = func(True)
