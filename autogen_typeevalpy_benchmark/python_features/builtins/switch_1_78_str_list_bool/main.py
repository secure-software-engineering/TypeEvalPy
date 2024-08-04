#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'hvybg':
            return [71, 54, 61]
        case [71, 54, 61]:
            return 'hvybg'
        case _:
            return "default"


a = func('hvybg')
b = func([71, 54, 61])
c = func(True)
