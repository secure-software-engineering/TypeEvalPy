#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'davmf': 90, 'cqsxm': 40, 'ukglh': 25}:
            return 'pruhj'
        case 'pruhj':
            return {'davmf': 90, 'cqsxm': 40, 'ukglh': 25}
        case _:
            return "default"


a = func({'davmf': 90, 'cqsxm': 40, 'ukglh': 25})
b = func('pruhj')
c = func(16)
