#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'bgkvs':
            return 45
        case 45:
            return 'bgkvs'
        case _:
            return "default"


a = func('bgkvs')
b = func(45)
c = func(20.05)
