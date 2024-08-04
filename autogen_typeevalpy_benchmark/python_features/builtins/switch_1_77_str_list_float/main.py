#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'zokck':
            return [35, 20, 56]
        case [35, 20, 56]:
            return 'zokck'
        case _:
            return "default"


a = func('zokck')
b = func([35, 20, 56])
c = func(13.48)
