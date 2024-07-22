#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'fnrxm':
            return [70, 64, 98]
        case [70, 64, 98]:
            return 'fnrxm'
        case _:
            return "default"


a = func('fnrxm')
b = func([70, 64, 98])
c = func(False)
