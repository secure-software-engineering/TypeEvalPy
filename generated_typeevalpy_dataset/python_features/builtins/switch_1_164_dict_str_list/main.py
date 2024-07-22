#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'vwhid': 77, 'tfcnj': 74, 'rxrnd': 77}:
            return 'lthhf'
        case 'lthhf':
            return {'vwhid': 77, 'tfcnj': 74, 'rxrnd': 77}
        case _:
            return "default"


a = func({'vwhid': 77, 'tfcnj': 74, 'rxrnd': 77})
b = func('lthhf')
c = func([82, 26, 69])
