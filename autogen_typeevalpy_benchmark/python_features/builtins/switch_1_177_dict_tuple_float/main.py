#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'jeeqg': 34, 'wulcw': 47, 'jnplg': 16}:
            return (80, 85, 97)
        case (80, 85, 97):
            return {'jeeqg': 34, 'wulcw': 47, 'jnplg': 16}
        case _:
            return "default"


a = func({'jeeqg': 34, 'wulcw': 47, 'jnplg': 16})
b = func((80, 85, 97))
c = func(57.17)
