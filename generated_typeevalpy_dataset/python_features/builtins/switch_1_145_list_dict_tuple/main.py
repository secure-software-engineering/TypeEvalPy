#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [91, 81, 14]:
            return {'lptks': 37, 'yhhqg': 5, 'qycvd': 57}
        case {'lptks': 37, 'yhhqg': 5, 'qycvd': 57}:
            return [91, 81, 14]
        case _:
            return "default"


a = func([91, 81, 14])
b = func({'lptks': 37, 'yhhqg': 5, 'qycvd': 57})
c = func((77, 34, 44))
