#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'rphwg':
            return 16
        case 16:
            return 'rphwg'
        case _:
            return "default"


a = func('rphwg')
b = func(16)
c = func([22, 69, 61])
