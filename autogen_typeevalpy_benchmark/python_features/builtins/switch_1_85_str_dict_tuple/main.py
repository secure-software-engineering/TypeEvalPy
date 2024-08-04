#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'zkdqj':
            return {'nhpvr': 95, 'zeefo': 81, 'pvnsy': 43}
        case {'nhpvr': 95, 'zeefo': 81, 'pvnsy': 43}:
            return 'zkdqj'
        case _:
            return "default"


a = func('zkdqj')
b = func({'nhpvr': 95, 'zeefo': 81, 'pvnsy': 43})
c = func((83, 22, 66))
