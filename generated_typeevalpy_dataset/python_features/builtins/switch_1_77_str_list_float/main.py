#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'cgiju':
            return [97, 28, 96]
        case [97, 28, 96]:
            return 'cgiju'
        case _:
            return "default"


a = func('cgiju')
b = func([97, 28, 96])
c = func(80.55)
