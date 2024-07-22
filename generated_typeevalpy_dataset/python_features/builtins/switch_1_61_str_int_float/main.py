#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'fqpub':
            return 20
        case 20:
            return 'fqpub'
        case _:
            return "default"


a = func('fqpub')
b = func(20)
c = func(94.07)
