#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [99, 24, 25]:
            return 'cfwmp'
        case 'cfwmp':
            return [99, 24, 25]
        case _:
            return "default"


a = func([99, 24, 25])
b = func('cfwmp')
c = func(True)
