#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'krjms':
            return [36, 13, 3]
        case [36, 13, 3]:
            return 'krjms'
        case _:
            return "default"


a = func('krjms')
b = func([36, 13, 3])
c = func(89)
