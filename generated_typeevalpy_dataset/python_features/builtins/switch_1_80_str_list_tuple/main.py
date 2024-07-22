#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'kimam':
            return [46, 50, 64]
        case [46, 50, 64]:
            return 'kimam'
        case _:
            return "default"


a = func('kimam')
b = func([46, 50, 64])
c = func((89, 84, 94))
