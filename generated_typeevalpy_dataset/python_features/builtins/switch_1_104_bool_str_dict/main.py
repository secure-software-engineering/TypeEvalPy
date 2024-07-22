#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'rhpta'
        case 'rhpta':
            return True
        case _:
            return "default"


a = func(True)
b = func('rhpta')
c = func({'yosnh': 26, 'cefsd': 53, 'gcgbi': 80})
