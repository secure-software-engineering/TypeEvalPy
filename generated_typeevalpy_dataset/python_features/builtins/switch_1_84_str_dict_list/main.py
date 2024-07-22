#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'hyydl':
            return {'ynpfp': 73, 'alujb': 87, 'owgss': 92}
        case {'ynpfp': 73, 'alujb': 87, 'owgss': 92}:
            return 'hyydl'
        case _:
            return "default"


a = func('hyydl')
b = func({'ynpfp': 73, 'alujb': 87, 'owgss': 92})
c = func([14, 58, 43])
