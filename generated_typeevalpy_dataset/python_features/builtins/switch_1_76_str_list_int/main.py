#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'izrjw':
            return [98, 72, 34]
        case [98, 72, 34]:
            return 'izrjw'
        case _:
            return "default"


a = func('izrjw')
b = func([98, 72, 34])
c = func(81)
