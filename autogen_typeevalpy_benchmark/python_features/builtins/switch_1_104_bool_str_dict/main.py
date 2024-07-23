#  A function is defined with switch statement in it.
def func(value):
    match value:
        case False:
            return 'azrmd'
        case 'azrmd':
            return False
        case _:
            return "default"


a = func(False)
b = func('azrmd')
c = func({'czqaq': 91, 'jtfbb': 96, 'cnque': 23})
