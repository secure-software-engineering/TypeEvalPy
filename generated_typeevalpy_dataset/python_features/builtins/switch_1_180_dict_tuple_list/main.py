#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'jvvsr': 57, 'wrncm': 11, 'vqfil': 57}:
            return (40, 45, 66)
        case (40, 45, 66):
            return {'jvvsr': 57, 'wrncm': 11, 'vqfil': 57}
        case _:
            return "default"


a = func({'jvvsr': 57, 'wrncm': 11, 'vqfil': 57})
b = func((40, 45, 66))
c = func([73, 73, 14])
