#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'unafg':
            return True
        case True:
            return 'unafg'
        case _:
            return "default"


a = func('unafg')
b = func(True)
c = func(14)
