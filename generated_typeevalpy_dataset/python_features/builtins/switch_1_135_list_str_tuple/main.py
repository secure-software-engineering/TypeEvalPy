#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [26, 5, 15]:
            return 'wgkag'
        case 'wgkag':
            return [26, 5, 15]
        case _:
            return "default"


a = func([26, 5, 15])
b = func('wgkag')
c = func((7, 98, 96))
