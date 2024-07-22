#  A function is defined with switch statement in it.
def func(value):
    match value:
        case True:
            return 'erwan'
        case 'erwan':
            return True
        case _:
            return "default"


a = func(True)
b = func('erwan')
c = func([2, 85, 60])
