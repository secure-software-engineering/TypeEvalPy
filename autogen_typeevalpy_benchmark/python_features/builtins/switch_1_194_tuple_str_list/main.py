#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (47, 2, 93):
            return 'kuebu'
        case 'kuebu':
            return (47, 2, 93)
        case _:
            return "default"


a = func((47, 2, 93))
b = func('kuebu')
c = func([10, 46, 94])
