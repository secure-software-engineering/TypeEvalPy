#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'pdafl':
            return [9, 57, 70]
        case [9, 57, 70]:
            return 'pdafl'
        case _:
            return "default"


a = func('pdafl')
b = func([9, 57, 70])
c = func({'zeezf': 56, 'gkmiz': 64, 'qjdng': 82})
