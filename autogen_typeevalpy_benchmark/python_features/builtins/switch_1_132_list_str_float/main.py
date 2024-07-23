#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [8, 82, 61]:
            return 'toazw'
        case 'toazw':
            return [8, 82, 61]
        case _:
            return "default"


a = func([8, 82, 61])
b = func('toazw')
c = func(62.04)
