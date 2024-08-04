#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'iitod':
            return 93
        case 93:
            return 'iitod'
        case _:
            return "default"


a = func('iitod')
b = func(93)
c = func([61, 98, 19])
