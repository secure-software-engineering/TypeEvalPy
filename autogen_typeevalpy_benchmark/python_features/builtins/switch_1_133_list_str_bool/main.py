#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [4, 95, 64]:
            return 'ulahj'
        case 'ulahj':
            return [4, 95, 64]
        case _:
            return "default"


a = func([4, 95, 64])
b = func('ulahj')
c = func(False)
