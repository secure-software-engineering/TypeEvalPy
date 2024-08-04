#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [94, 69, 35]:
            return 'qrzls'
        case 'qrzls':
            return [94, 69, 35]
        case _:
            return "default"


a = func([94, 69, 35])
b = func('qrzls')
c = func(44.68)
