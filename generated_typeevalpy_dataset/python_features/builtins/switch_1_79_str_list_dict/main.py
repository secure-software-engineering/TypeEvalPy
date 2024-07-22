#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'lilwb':
            return [22, 83, 5]
        case [22, 83, 5]:
            return 'lilwb'
        case _:
            return "default"


a = func('lilwb')
b = func([22, 83, 5])
c = func({'ceqfw': 73, 'gccyt': 33, 'pnjwy': 30})
