#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'ihenc': 80, 'jfcrr': 85, 'ayivr': 93}:
            return (81, 58, 23)
        case (81, 58, 23):
            return {'ihenc': 80, 'jfcrr': 85, 'ayivr': 93}
        case _:
            return "default"


a = func({'ihenc': 80, 'jfcrr': 85, 'ayivr': 93})
b = func((81, 58, 23))
c = func('vhhzw')
