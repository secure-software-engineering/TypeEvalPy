#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 86:
            return 'hhijn'
        case 'hhijn':
            return 86
        case _:
            return "default"


a = func(86)
b = func('hhijn')
c = func((90, 10, 9))
