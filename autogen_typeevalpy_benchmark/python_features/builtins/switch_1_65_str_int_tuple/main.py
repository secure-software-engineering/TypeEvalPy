#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'wfmrd':
            return 28
        case 28:
            return 'wfmrd'
        case _:
            return "default"


a = func('wfmrd')
b = func(28)
c = func((78, 69, 11))
