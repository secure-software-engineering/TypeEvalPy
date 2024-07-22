#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'nyuat': 55, 'mhcbu': 20, 'bhxmo': 63}:
            return 18
        case 18:
            return {'nyuat': 55, 'mhcbu': 20, 'bhxmo': 63}
        case _:
            return "default"


a = func({'nyuat': 55, 'mhcbu': 20, 'bhxmo': 63})
b = func(18)
c = func([69, 25, 71])
