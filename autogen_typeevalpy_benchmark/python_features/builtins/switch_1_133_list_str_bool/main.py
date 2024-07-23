#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [48, 52, 13]:
            return 'qjtlk'
        case 'qjtlk':
            return [48, 52, 13]
        case _:
            return "default"


a = func([48, 52, 13])
b = func('qjtlk')
c = func(True)
