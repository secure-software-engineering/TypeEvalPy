#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (96, 62, 69):
            return {'qvjef': 77, 'bvbgk': 81, 'ltpca': 53}
        case {'qvjef': 77, 'bvbgk': 81, 'ltpca': 53}:
            return (96, 62, 69)
        case _:
            return "default"


a = func((96, 62, 69))
b = func({'qvjef': 77, 'bvbgk': 81, 'ltpca': 53})
c = func(True)
