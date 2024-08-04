#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'zvmct': 17, 'rzisr': 16, 'daore': 100}:
            return 47
        case 47:
            return {'zvmct': 17, 'rzisr': 16, 'daore': 100}
        case _:
            return "default"


a = func({'zvmct': 17, 'rzisr': 16, 'daore': 100})
b = func(47)
c = func('qoqxt')
