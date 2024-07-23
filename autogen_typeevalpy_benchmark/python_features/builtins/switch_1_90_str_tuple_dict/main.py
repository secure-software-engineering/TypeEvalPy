#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'hqwby':
            return (42, 4, 14)
        case (42, 4, 14):
            return 'hqwby'
        case _:
            return "default"


a = func('hqwby')
b = func((42, 4, 14))
c = func({'brsol': 63, 'jtzbs': 27, 'pyvyr': 70})
