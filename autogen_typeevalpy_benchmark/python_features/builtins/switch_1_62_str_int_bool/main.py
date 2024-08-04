#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'hkbqc':
            return 16
        case 16:
            return 'hkbqc'
        case _:
            return "default"


a = func('hkbqc')
b = func(16)
c = func(True)
