#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'aufst': 46, 'lmuul': 95, 'hngpj': 49}:
            return 'facov'
        case 'facov':
            return {'aufst': 46, 'lmuul': 95, 'hngpj': 49}
        case _:
            return "default"


a = func({'aufst': 46, 'lmuul': 95, 'hngpj': 49})
b = func('facov')
c = func(True)
