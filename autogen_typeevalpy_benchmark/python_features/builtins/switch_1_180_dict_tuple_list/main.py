#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'qivxs': 63, 'pjvpl': 55, 'kagnb': 77}:
            return (83, 14, 18)
        case (83, 14, 18):
            return {'qivxs': 63, 'pjvpl': 55, 'kagnb': 77}
        case _:
            return "default"


a = func({'qivxs': 63, 'pjvpl': 55, 'kagnb': 77})
b = func((83, 14, 18))
c = func([74, 10, 38])
