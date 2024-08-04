#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 54.15:
            return 'lblki'
        case 'lblki':
            return 54.15
        case _:
            return "default"


a = func(54.15)
b = func('lblki')
c = func(True)
