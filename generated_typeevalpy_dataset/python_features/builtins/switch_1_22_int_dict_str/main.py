#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 95:
            return {'hdznd': 9, 'vmxit': 8, 'eumzg': 84}
        case {'hdznd': 9, 'vmxit': 8, 'eumzg': 84}:
            return 95
        case _:
            return "default"


a = func(95)
b = func({'hdznd': 9, 'vmxit': 8, 'eumzg': 84})
c = func('bprog')
