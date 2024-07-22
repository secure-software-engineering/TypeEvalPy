#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'kjaus':
            return (89, 64, 77)
        case (89, 64, 77):
            return 'kjaus'
        case _:
            return "default"


a = func('kjaus')
b = func((89, 64, 77))
c = func(91.55)
