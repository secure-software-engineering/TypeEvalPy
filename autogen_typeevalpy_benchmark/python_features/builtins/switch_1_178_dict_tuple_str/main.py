#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'bgrte': 22, 'ledww': 68, 'cclos': 96}:
            return (28, 22, 50)
        case (28, 22, 50):
            return {'bgrte': 22, 'ledww': 68, 'cclos': 96}
        case _:
            return "default"


a = func({'bgrte': 22, 'ledww': 68, 'cclos': 96})
b = func((28, 22, 50))
c = func('matcl')
