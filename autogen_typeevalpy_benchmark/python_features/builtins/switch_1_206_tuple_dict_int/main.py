#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (83, 37, 22):
            return {'tcose': 83, 'qhgcj': 79, 'eczkt': 23}
        case {'tcose': 83, 'qhgcj': 79, 'eczkt': 23}:
            return (83, 37, 22)
        case _:
            return "default"


a = func((83, 37, 22))
b = func({'tcose': 83, 'qhgcj': 79, 'eczkt': 23})
c = func(33)
