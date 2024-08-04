#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [35, 10, 32]:
            return 'vkrdn'
        case 'vkrdn':
            return [35, 10, 32]
        case _:
            return "default"


a = func([35, 10, 32])
b = func('vkrdn')
c = func(56)
