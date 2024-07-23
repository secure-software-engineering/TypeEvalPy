#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'xlhfe'
        case 'xlhfe':
            return True
        case _:
            return "default"


a = func(True)
b = func('xlhfe')
c = func(4.37)
