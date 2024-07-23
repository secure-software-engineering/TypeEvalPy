#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'ssnve':
            return 34.15
        case 34.15:
            return 'ssnve'
        case _:
            return "default"


a = func('ssnve')
b = func(34.15)
c = func(False)
