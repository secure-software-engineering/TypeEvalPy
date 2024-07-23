#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'fyueh':
            return 74.12
        case 74.12:
            return 'fyueh'
        case _:
            return "default"


a = func('fyueh')
b = func(74.12)
c = func((89, 12, 92))
